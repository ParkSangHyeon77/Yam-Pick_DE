import pymysql

conn = pymysql.connect(host='smooth.mysql.pythonanywhere-services.com',
                    port=3306,
                    user='smooth',
                    passwd='weareking!',
                    db='smooth$yampick',
                    charset='utf8')

cur = conn.cursor()

cur.execute("""CREATE TABLE test2(
				    AlbumId INTEGER NOT NULL PRIMARY KEY,
				    Title NVARCHAR(160),
                    ArtistId INTEGER);
			""")

conn.commit()

conn.close()