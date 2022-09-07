from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from datetime import datetime

from yp import db
from yp.forms import UserCreateForm
from yp.models import tb_user, tb_user_info

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    global form
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = tb_user.query.filter_by(user_email=form.email.data).first()
        if not email:
            useremail = form.email.data
            user = tb_user(user_name=form.username.data,
                        user_pw=generate_password_hash(form.password1.data),
                        user_email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.more_info'))
        else:
            flash('이미 존재하는 이메일입니다.')
    return render_template('auth/signup.html', form=form)

@bp.route('/more_info/', methods=('GET', 'POST'))
def more_info():
    today = datetime.now().date()
    if request.method == 'POST':
        user = tb_user_info(user_email=form.email.data,
                            user_weight=form.user_weight.data,
                            user_height=form.user_height.data,
                            user_birth=form.user_birth.data,
                            user_cal=form.user_cal.data,
                            user_goal=form.user_goal.data,
                            user_sex=form.user_sex.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.main'))
    return render_template('auth/more_info.html', form=form, today=today)
