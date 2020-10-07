import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="luminarpython",
    passwd="Password@123",
    auth_plugin='mysql_native_password'

)

cursor=db.cursor()

query="INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,SEX,AGE,SALARY)VALUES('VAY','AN','M',24,20000)"
try:
    cursor.execute(query)
    db.commit()
except Exception as e:
    db.rollback()#partial changes
    print(e.args)
finally:
    db.close()