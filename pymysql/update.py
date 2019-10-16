import pymysql

db = pymysql.connect(host='35.188.0.65', port=3306, user='root', passwd='gus', db='gcp', charset='utf8')
try:
    with db.cursor() as cursor:
        sql = "UPDATE korea SET model_type='%s' WHERE name = 'i5'" % 'karviee'
        cursor.execute(sql)
        db.commit()
        print(cursor.rowcount)
finally:
    db.close()
