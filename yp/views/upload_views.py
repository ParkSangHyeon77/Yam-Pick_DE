from flask import Blueprint, render_template, request, url_for, redirect
from yp.models import tb_user_img
from yp import db
from sqlalchemy import func

bp = Blueprint('upload', __name__, url_prefix='/upload')


@bp.route('/')
def upload():
    return render_template("upload.html")

@bp.route("/", methods=["POST"])
def upload_done():
    # NEW_IMG = tb_user_img(upload_user = '',
    #                     upload_foodname = '',
    #                     upload_location = '',
    #                     upload_isnew = True)
    
    NEW_IMG = tb_user_img()
    print(db.session.query(func.count(tb_user_img.upload_index)).all()[0][0])
    NEW_IMG.upload_index = db.session.query(func.count(tb_user_img.upload_index)).all()[0][0] + 1
    NEW_IMG.upload_user = '지현'
    NEW_IMG.upload_foodname = '된장찌개'
    NEW_IMG.upload_location = f"yp/static/img/{NEW_IMG.upload_index}.jpeg"
    NEW_IMG.upload_isnew = True

    db.session.add(NEW_IMG)
    
    db.session.commit()

    uploaded_files = request.files["food_img"]
    uploaded_files.save(NEW_IMG.upload_location)

    return redirect(url_for("upload.upload"))