import mysql.connector

def get_connection():
    return mysql.connector.connect(
         host="localhost",
         port=3306,
         uesr="sunbeam",
         password="sunbeam",
         database="iotdb"
    )

def update_person(empid,salary):
    conn=get_connection()

    query=f"update employe SET salary=%f where empid=%f;"
    val=(salary,empid)

    cursor=conn.cursor()
    cursor.execute(query,val)
    cursor.commit()
    cursor.close()
    conn.close()

update_person(10,50700)
