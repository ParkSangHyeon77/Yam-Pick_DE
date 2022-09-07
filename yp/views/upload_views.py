from flask import Blueprint, render_template, request, url_for, redirect
from yp.models import tb_user_img
from yp import db
from sqlalchemy import func

from yp.views.auth_views import session
from yp.models import tb_user


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


    # NEW_IMG.upload_location = f"/home/smooth/Yam-Pick_DE/yp/static/img/{NEW_IMG.upload_index}.jpeg"
    NEW_IMG.upload_location = f"yp/static/img/{NEW_IMG.upload_index}.jpeg"

    uploaded_files = request.files["food_img"]
    uploaded_files.save(NEW_IMG.upload_location)

    # DS 결과
    global model_result
    model_result = ['김치찌개', '부대찌개', '등갈비', '냉면', '시리얼']

    return render_template("upload_check.html", first = model_result[0], photo = f"img/{NEW_IMG.upload_index}.jpeg")

@bp.route("/re")
def double_check():
    if NEW_IMG:
        return render_template("upload_check2.html", food_list = model_result[1:], photo = f"img/{NEW_IMG.upload_index}.jpeg")

    else:
        return render_template("error.html") # 에러 페이지 만들거나 홈으로 돌아가기


@bp.route("/how", methods=["POST"])
def how():
    if NEW_IMG:
        NEW_IMG.upload_foodname = request.form["food_name"]

        # 이미 가지고 있는 음식 목록에 있다면
        if NEW_IMG.upload_foodname in ['김치찌개', '된장찌개']:
            NEW_IMG.upload_isnew = False
        else:
            NEW_IMG.upload_isnew = True
        db.session.add(NEW_IMG)
        db.session.commit()
        return render_template("upload_how.html", photo = f"img/{NEW_IMG.upload_index}.jpeg")
    else:
        return render_template("error.html")
@bp.route("/result", methods=["POST"])
def result():
    if NEW_IMG.upload_isnew:
        return "해당 음식이 존재하지 않습니다."
    else:
        RATIO = float(request.form["ratio"])

        # 해당 음식의 칼로리 가져오기
        CAL = 5000

        # 기초대사량 가져오기
        user_cal = 7000

        # 칼로리 계산
        res = user_cal - 250 - CAL * RATIO

        # 계산하는 코드

        return render_template("upload_result.html")

