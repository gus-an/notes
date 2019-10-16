import pymysql

db = pymysql.connect(host='35.188.0.65', port=3306, user='root', passwd='gus', db='gcp', charset='utf8')
try:
    with db.cursor() as cursor:
        sql = "DELETE FROM korea WHERE id = '%s'" % '17'
        cursor.execute(sql)
        db.commit()
        print(cursor.rowcount)
finally:
    db.close()
