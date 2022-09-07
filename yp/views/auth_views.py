from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from datetime import datetime

from yp import db
from yp.forms import UserCreateForm, UserLoginForm
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

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = tb_user.query.filter_by(user_email=form.email.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.user_pw, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user'] = user.user_email
            return redirect(url_for('main.main'))
        flash(error)
    return render_template('auth/login.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_email = session.get('user')
    if user_email is None:
        g.user = None
    else:
        g.user = tb_user.query.get(user_email)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.main'))