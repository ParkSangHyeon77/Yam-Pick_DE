from flask import Flask
from sqlalchemy import create_engine




app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{username}:{password}@{hostname}/{databasename}".format(
    username='smooth',
    password='weareking!',
    hostname='smooth.mysql.pythonanywhere-services.com',
    databasename='smooth$yampick',
)

SQLALCHEMY_TRACK_MODIFICATIONS = False

# engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=280)