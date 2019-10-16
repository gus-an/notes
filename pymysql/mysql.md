# 0. Troubleshoot
```
systemctl status mysql.service
```
- 데이터베이스 control commands
```
sudo service mysql start
sudo service mysql restart
sudo service mysql stop
```
- stop 을 해도 DB 내용은 사라지지 않는다.

# 1. Commands to Init

```
sudo apt-get update
sudo apt-get install mysql-server

sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```
source: https://www.fun-coding.org/mysql_basic2.html 
Add
```
collation-server = utf8_unicode_ci
character-set-server = utf8
skip-character-set-client-handshake
bind-address            = 0.0.0.0   
```
```
sudo service mysql start
sudo mysql
mysql> use mysql;
mysql> GRANT ALL PRIVILEGES ON *.* to 'root'@'%' IDENTIFIED BY 'gus';
mysql> flush privileges;
mysql> exit
sudo service mysql restart
```
+ open port 3306 for the server running mysql
Now, anyone can access this database using
```
mysql -h 35.188.0.65 -u root -p gcp
```
where user = host, passwd = gus

# 2. Create table
```
mysql> CREATE DATABASE gcp;
mysql> SHOW DATABASES;
mysql> USE gcp;
mysql> SHOW TABLES;
mysql> CREATE TABLE poe (name VARCHAR(20), level INT(20));
mysql> DESCRIBE poe;
mysql> INSERT INTO poe VALUES ('gus', 200);
mysql> SELECT * FROM poe;
```
