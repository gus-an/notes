import pymysql

db = pymysql.connect(host='35.188.0.65', port=3306, user='root', passwd='gus', db='gcp', charset='utf8')
try:
    cursor = db.cursor()
    sql = "SELECT * FROM korea"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row_data in result:
        print(row_data[0])
        print(row_data[1])
        print(row_data[2])
        print(row_data[3]) 
finally:
    db.close()
