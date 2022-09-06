from flask import Flask
from sqlalchemy import create_engine


# SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{username}:{password}@{hostname}/{databasename}".format(
#     username='smooth',
#     password='weareking!',
#     hostname='smooth.mysql.pythonanywhere-services.com',
#     databasename='smooth$yampick',
# )

# SQLALCHEMY_TRACK_MODIFICATIONS = False


# engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=280)

import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False