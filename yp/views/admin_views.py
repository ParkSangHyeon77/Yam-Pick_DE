from flask import Blueprint, render_template, session
import base_database

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
def admin():
   base_database.base_database()
   return "완료"