from flask import Flask
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'smooth.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'smooth'
app.config['MYSQL_PASSWORD'] = 'weareking!'
app.config['MYSQL_DB'] ='smooth$yampick'
app.config['MYSQL_PORT'] = 33906

mysql=MySQL(app)

cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute('CREATE * TABLE TEST2')

cursor.commit()
cursor.close()