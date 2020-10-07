import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin='mysql_native_password'

)#open database connection
#create a cursor object(object that carry data to mysql from python and viseversa)
cursor=db.cursor()

#execute mysql query using execute() method
sql="SELECT VERSION()"
cursor.execute(sql)

#fetch a single row using fetchone() method
data=cursor.fetchone()
print("Database version:",data)

#disconnect from server
db.close()