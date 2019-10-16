import pymysql

db = pymysql.connect(host='35.188.0.65', port=3306, user='root', passwd='gus', db='gcp', charset='utf8')
try:
    with db.cursor() as cursor:
        sql = '''
            CREATE TABLE korea (
                   id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                   name VARCHAR(20) NOT NULL,
                   model_num VARCHAR(10) NOT NULL,
                   model_type VARCHAR(10) NOT NULL,
                   PRIMARY KEY(id)
            );
        '''
        cursor.execute(sql)
        db.commit()
finally:
    db.close()
