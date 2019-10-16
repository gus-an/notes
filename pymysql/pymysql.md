# 1. Install
```
sudo apt-get install python3-pip
pip3 install PyMySQL
```

# 2. Run
```
import pymysql

db = pymysql.connect(host='35.188.0.65', port=3306, user='root', passwd='gus', db='gcp', charset='utf8')

db

cursor = db.cursor()

cursor

sql = """
... SELECT * FROM poe; 
... """

cursor.execute(sql)
```
```
db.commit()
db.close()
```

# meanings
- `cursor.lastrowid`
    - INSERT 나 UPDATE 문에서 AUTO_INCREMENT 값에 해당하는 마지막 값을 반환.
- `cursor.execute(sql)`
    - SELECT 문이라면, 반환하는 값을 개수를 반환
- Fetch
    - `cursor.fetchall()`: fetch all the rows
    - `cursor.fetchmany(size=None)`: Fetch several rows
    - `cursor.fetchone()`: Fet the next row
- `cursor.rowcount`
    - UPDATE 문에서는 반영된 row 개수 반환