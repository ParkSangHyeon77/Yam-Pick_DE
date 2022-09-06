from flask import Blueprint, render_template, request, url_for, redirect
from yp.models import tb_user_img
from yp import db
from sqlalchemy import func

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
    NEW_IMG.upload_user = '지현'

    # if 가이드라인에 맞지 않음:
        # return redirect(url_for("upload.upload"))

    # else
    NEW_IMG.upload_location = f"yp/static/img/{NEW_IMG.upload_index}.jpeg"

    uploaded_files = request.files["food_img"]
    uploaded_files.save(NEW_IMG.upload_location)

    # DS 결과
    global model_result
    model_result = ['김치찌개', '부대찌개', '등갈비', '냉면', '시리얼']

    return render_template("upload_check.html", first = model_result[0])

@bp.route("/re")
def double_check():
    if NEW_IMG:
        return render_template("upload_check2.html", food_list = model_result[1:])

    else:
        return "잘못된 접근입니다." # 에러 페이지 만들거나 홈으로 돌아가기


@bp.route("/how")
def how():
    NEW_IMG.upload_foodname = request.args.get("food_name")
    NEW_IMG.upload_isnew = True
    db.session.add(NEW_IMG)
    db.session.commit()
    return NEW_IMG.upload_foodname

