import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="luminarpython",
    passwd="Password@123",
    auth_plugin='mysql_native_password'

)

cursor=db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql="CREATE TABLE EMPLOYEE (FIRST_NAME CHAR(20),LAST_NAME CHAR(20),SEX CHAR(2),AGE INT,SALARY INT)"

cursor.execute(sql)

db.close()

