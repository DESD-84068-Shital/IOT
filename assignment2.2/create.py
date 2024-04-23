import mysql.connector

connection=mysql.connector.connect(
   host="localhost",
   port=3306,
   user="sunbeam",
   password="sunbeam",
   database="iotdb"
)

empid=int(input("Enter empid:"))
name=input("Enter name:")
department=input("Enter department:")
email=input("Enter email:")
salary=float(input("Enter salary:"))
date_of_joining=input("Enter date_of_joining:")

query=f"insert into employe values({empid},'{name}','{department}','{email}','{salary}','{date_of_joining}')"

cursor=connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()
