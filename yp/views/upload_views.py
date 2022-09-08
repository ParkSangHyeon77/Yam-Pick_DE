from flask import Blueprint, render_template, request, url_for, redirect, session, g
from yp.models import tb_user_img
from yp import db
from sqlalchemy import func

from yp.models import tb_user, tb_food_img
import func_user__nutrient
import func_ml


bp = Blueprint('upload', __name__, url_prefix='/upload')
NEW_IMG = None


@bp.route('/')
def upload():
    return render_template("upload.html")

@bp.route("/", methods=["POST"])
def upload_done():
    
    global NEW_IMG
    NEW_IMG = tb_user_img()
    NEW_IMG.upload_index = db.session.query(func.count(tb_user_img.upload_index)).all()[0][0] + 1
    NEW_IMG.upload_user = 'geehyun'

    # if 가이드라인에 맞지 않음:
        # return redirect(url_for("upload.upload"))

    # else


    # NEW_IMG.upload_location = f"/home/smooth/Yam-Pick_DE/yp/static/img/user_upload/{NEW_IMG.upload_index}.jpg"
    NEW_IMG.upload_location = f"yp/static/img/user_upload/{NEW_IMG.upload_index}.jpg"

    uploaded_files = request.files["food_img"]
    uploaded_files.save(NEW_IMG.upload_location)

    # DS 결과
    # model_result = func_ml.image_prediction_result(NEW_IMG.upload_location, model_dir, model_name)

    global model_result
    model_result = ['김치찌개', '부대찌개', '등갈비', '냉면', '시리얼']

    # return render_template("upload_check.html", first = model_result["TOP1"], photo = f"img/user_upload/{NEW_IMG.upload_index}.jpg")

    return render_template("upload_check.html", first = model_result[0], photo = f"img/user_upload/{NEW_IMG.upload_index}.jpg")

@bp.route("/re")
def double_check():
    if NEW_IMG:
        # return render_template("upload_check2.html", food_list = model_result["TOP2to5"], photo = f"img/user_upload/{NEW_IMG.upload_index}.jpg")
        return render_template("upload_check2.html", food_list = model_result[1:], photo = f"img/user_upload/{NEW_IMG.upload_index}.jpg")

    else:
        return render_template("error.html") # 에러 페이지 만들거나 홈으로 돌아가기


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
            return render_template("upload_how.html", photo = f"img/user_upload/{NEW_IMG.upload_index}.jpg")
        else:
            NEW_IMG.upload_isnew = True
            db.session.add(NEW_IMG)
            db.session.commit()
            return "해당 음식이 존재하지 않습니다."

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

    max_remain_ratio = 0
    for nutrient in user_nutrient_dic:
        remain_ratio = (user_nutrient_dic[nutrient] - food_being[nutrient] * RATIO) / user_nutrient_dic[nutrient]
        if max_remain_ratio < remain_ratio:
            max_remain_nutrient = nutrient
            max_remain = user_nutrient_dic[nutrient] - food_being[nutrient] * RATIO

    text = f"가장 부족한 영양소는 {func_user__nutrient.en_ko_dict[max_remain_nutrient]}이며, {max_remain}만큼 더 섭취해야 합니다."

#    res_list = db.session.query(tb_food_img).filter(float(max_remain_nutrient) > max_remain - user_nutrient_dic[max_remain_nutrient] * 0.1) #, max_remain))
    
#    return render_template("upload_result.html", text=text, res_list=res_list)
    return text