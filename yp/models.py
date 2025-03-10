from yp import db

class tb_user(db.Model):
    user_email = db.Column(db.String(45), primary_key=True)
    user_pw = db.Column(db.String(45), nullable=False)
    user_name = db.Column(db.String(16), nullable=False)
    user_status = db.Column(db.SmallInteger, nullable=True)

class tb_user_info(db.Model):
    user_email = db.Column(db.String(45), db.ForeignKey('tb_user.user_email', ondelete='CASCADE'), primary_key=True)
    user_weight = db.Column(db.FLOAT(10), nullable=True)
    user_height = db.Column(db.FLOAT(10), nullable=True)
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
    def __getitem__(self,key):
        return getattr(self, key)
    food_index = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(45), nullable=False)
    food_img = db.Column(db.String(45), nullable=True)
    energy = db.Column(db.FLOAT(10), nullable=True)
    carbohydrate = db.Column(db.FLOAT(10), nullable=True)
    fat = db.Column(db.FLOAT(10), nullable=True)
    protein = db.Column(db.FLOAT(10), nullable=True)
    moisture = db.Column(db.FLOAT(10), nullable=True)
    vitamin_A = db.Column(db.FLOAT(10), nullable=True)
    vitamin_D = db.Column(db.FLOAT(10), nullable=True)
    vitamin_E = db.Column(db.FLOAT(10), nullable=True)
    vitamin_C = db.Column(db.FLOAT(10), nullable=True)
    folic_acid = db.Column(db.FLOAT(10), nullable=True)
    phosphorus = db.Column(db.FLOAT(10), nullable=True)
    sodium = db.Column(db.FLOAT(10), nullable=True)
    potassium = db.Column(db.FLOAT(10), nullable=True)
    manganese = db.Column(db.FLOAT(10), nullable=True)
    selenium = db.Column(db.FLOAT(10), nullable=True)
    dietary_fiber = db.Column(db.FLOAT(10), nullable=True)
    thiamin = db.Column(db.FLOAT(10), nullable=True)
    riboflavin = db.Column(db.FLOAT(10), nullable=True)
    niacin = db.Column(db.FLOAT(10), nullable=True)
    calcium = db.Column(db.FLOAT(10), nullable=True)
    magnesium = db.Column(db.FLOAT(10), nullable=True)
    iron = db.Column(db.FLOAT(10), nullable=True)
    zinc = db.Column(db.FLOAT(10), nullable=True)
    copper = db.Column(db.FLOAT(10), nullable=True)
    linolenic_acid = db.Column(db.FLOAT(10), nullable=True)
    a_linolenic_acid = db.Column(db.FLOAT(10), nullable=True)
    unsaturated_fatty_aci = db.Column(db.FLOAT(10), nullable=True)

class tb_board(db.Model):
    brd_index = db.Column(db.Integer, primary_key=True)
    brd_user = db.Column(db.String(45), nullable=False)
    brd_title = db.Column(db.String(45), nullable=False)
    brd_content = db.Column(db.Text(), nullable=False)
