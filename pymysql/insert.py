import pymysql

db = pymysql.connect(host='35.188.0.65', port=3306, user='root', passwd='gus', db='gcp', charset='utf8')
try:
    cursor = db.cursor()
    for num in range(10, 20):
        sql = "INSERT INTO korea (id, name, model_num, model_type) VALUES(" + str(num) + ", 'i5', '7700', 'Kaby Lake')"
        print(sql)
        cursor.execute(sql)

    db.commit()
    print(cursor.lastrowid)
finally:
    db.close()
