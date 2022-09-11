from flask import Blueprint, render_template, request, g
from functions.base_database import base_database

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/', methods=["GET", "POST"])
def admin():
    if g.user.user_email == "miso324@naver.com":
        if request.method == 'POST':
            base_database()
            return "추천 음식 업로드 완료"
        return render_template('admin.html')
    else:
        return render_template("error.html")