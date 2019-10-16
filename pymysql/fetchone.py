import pymysql

db = pymysql.connect(host='35.188.0.65', port=3306, user='root', passwd='gus', db='gcp', charset='utf8')
try:
    with db.cursor() as cursor:
        sql = "SELECT * FROM korea WHERE name = 'i5'"
        cursor.execute(sql)
        
        result = cursor.fetchone()        
        while result:
            print(result)    
            result = cursor.fetchone()
finally:
    db.close()
