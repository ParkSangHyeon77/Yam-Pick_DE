from yp import db

class tb_user(db.Model):
    user_email = db.Column(db.String(45), primary_key=True)
    user_pw = db.Column(db.String(45), nullable=False)
    user_name = db.Column(db.String(16), nullable=False)

class tb_user_info(db.Model):
    user_email = db.Column(db.String(45), db.ForeignKey('tb_user.user_email', ondelete='CASCADE'), primary_key=True)
    user_weight = db.Column(db.FLOAT(10), nullable=True)
    user_height = db.Column(db.SmallInteger, nullable=True)
    user_birth = db.Column(db.Date, nullable=True)
    user_cal = db.Column(db.FLOAT(10), nullable=True)
    user_goal = db.Column(db.FLOAT(10), nullable=True)
    user_sex = db.Column(db.Boolean, nullable=True)
    user_pa = db.Column(db.SmallInteger, nullable=True)

class tb_user_img(db.Model):
    upload_index = db.Column(db.Integer, primary_key=True)
    upload_user = db.Column(db.String(45), db.ForeignKey('tb_user.user_email', ondelete='SET NULL'))
    upload_foodname = db.Column(db.String(45), nullable=False)
    upload_location = db.Column(db.String(45), nullable=False)
    upload_isnew = db.Column(db.Boolean, nullable=False)

class tb_food_img(db.Model):
    food_index = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(45), nullable=False)
    food_cal = db.Column(db.FLOAT(10), nullable=True)
    food_img = db.Column(db.String(45), nullable=False)

class tb_board(db.Model):
    brd_index = db.Column(db.Integer, primary_key=True)
    brd_user = db.Column(db.String(45), nullable=False)
    brd_title = db.Column(db.String(45), nullable=False)
    brd_content = db.Column(db.Text(), nullable=False)
