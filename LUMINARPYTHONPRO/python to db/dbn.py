import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="luminarpython",
    passwd="Password@123",
    auth_plugin='mysql_native_password'

)

cursor=db.cursor()
try:
    query="SELECT LAST_NAME FROM EMPLOYEE WHERE SALARY>20000"
    cursor.execute(query)
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)

except Exception as e:
    print(e.args)
finally:
    db.close()