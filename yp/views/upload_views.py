from flask import Blueprint, render_template, request, g
from yp.models import tb_user_img, tb_food_img
from yp import db
from sqlalchemy import func, and_
from functions import func_ml, func_user__nutrient

import config
import os


bp = Blueprint('upload', __name__, url_prefix='/upload')
NEW_IMG = None


@bp.route('/')
def upload():
    return render_template("upload/upload.html")

@bp.route("/", methods=["POST"])
def upload_done():
    
    global NEW_IMG
    NEW_IMG = tb_user_img()
    NEW_IMG.upload_index = db.session.query(func.count(tb_user_img.upload_index)).all()[0][0] + 1
    NEW_IMG.upload_user = 'geehyun'

    NEW_IMG.upload_location = os.path.join(config.BASE_DIR, f"yp/static/img/user_upload/{NEW_IMG.upload_index}.jpg")

    uploaded_files = request.files["food_img"]
    uploaded_files.save(NEW_IMG.upload_location)

    # DS 결과
    global model_result
    model_result = func_ml.image_prediction_result(NEW_IMG.upload_location, './', 'DenseNet201_129menu.h5')

    return render_template("upload/upload_check.html", first = model_result["TOP1"], photo = f"img/user_upload/{NEW_IMG.upload_index}.jpg")

@bp.route("/re")
def double_check():
    if NEW_IMG:
        return render_template("upload/upload_check2.html", food_list = model_result["TOP2to5"], photo = f"img/user_upload/{NEW_IMG.upload_index}.jpg")
        
    else:
        return render_template("error.html")


@bp.route("/how", methods=["POST"])
def how():
    if NEW_IMG:
        NEW_IMG.upload_foodname = request.form["food_name"].replace(" ", "")

        # 이미 가지고 있는 음식 목록에 있다면
        food_being = tb_food_img.query.filter_by(food_name=NEW_IMG.upload_foodname).first()
        if food_being:
            NEW_IMG.upload_isnew = False
            db.session.add(NEW_IMG)
            db.session.commit()
            return render_template("upload/upload_how.html", photo = f"img/user_upload/{NEW_IMG.upload_index}.jpg")
        else:
            NEW_IMG.upload_isnew = True
            db.session.add(NEW_IMG)
            db.session.commit()
            return render_template("upload/upload_isnew.html")

    else:
        return render_template("error.html")

@bp.route("/result", methods=["POST"])
def result():
    food_being = tb_food_img.query.filter_by(food_name=NEW_IMG.upload_foodname).first()

    RATIO = float(request.form["ratio"])

    # 사용자
    user_age = func_user__nutrient.user_age(g.user_info.user_birth, )

    weight_s = func_user__nutrient.standard_weight(g.user_info.user_sex, g.user_info.user_height)
    weight_a = func_user__nutrient.adjusted_weight(g.user_info.user_weight, weight_s)
    user_calorie = func_user__nutrient.calorie_counting(g.user_info.user_sex, user_age, g.user_info.user_height, weight_a, str(g.user_info.user_pa))
    user_nutrient_dic = func_user__nutrient.necessary_nutrients(g.user_info.user_sex, user_age, g.user_info.user_weight, user_calorie)

    remain_dict = {}
    overdose = []
    for nutrient in user_nutrient_dic:
        remain_dict[nutrient] = max(user_nutrient_dic[nutrient] - food_being[nutrient] * RATIO, 0)
        if remain_dict[nutrient] == 0:
            overdose.append(nutrient)
        
    text = f"오늘 {', '.join(list(map(lambda en: func_user__nutrient.en_ko_dict[en], overdose)))}(을)를 너무 많이 섭취했어요!"

    res_list = db.session.query(tb_food_img).filter(and_(tb_food_img.vitamin_A <= remain_dict['vitamin_A'],
                                                        tb_food_img.vitamin_D <= remain_dict['vitamin_D'],
                                                        tb_food_img.vitamin_E <= remain_dict['vitamin_E'],
                                                        tb_food_img.calcium <= remain_dict['calcium'],
                                                        tb_food_img.iron <= remain_dict['iron'],
                                                        tb_food_img.magnesium <= remain_dict['magnesium'],
                                                        tb_food_img.phosphorus <= remain_dict['phosphorus'],
                                                        tb_food_img.potassium <= remain_dict['potassium'],
                                                        tb_food_img.sodium <= remain_dict['sodium'],
                                                        tb_food_img.zinc <= remain_dict['zinc'],
                                                        tb_food_img.copper <= remain_dict['copper']
                                                        )
                                                    ).all()

    return render_template("upload/upload_result.html", text=text, res_list=res_list)