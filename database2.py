import pymysql
import MySQLdb.cursors

conn = pymysql.connect(host='smooth.mysql.pythonanywhere-services.com',
                    port=3306,
                    user='smooth',
                    passwd='weareking!',
                    db='smooth$yampick',
                    charset='utf8')

cur = conn.cursor(MySQLdb.cursors.DictCursor)

cur.execute("""CREATE TABLE if not exists tb_user(
                    user_email VARCHAR(45) NOT NULL PRIMARY KEY,
                    user_pw VARCHAR(45) NOT NULL,
                    user_name VARCHAR(16) NOT NULL);
			""")

conn.commit()

conn.close()