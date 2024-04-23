import mysql.connector

connection=mysql.connector.connect(
   host="localhost",
   port=3306,
   user="sunbeam",
   password="sunbeam",
   database="iotdb"
)


def delete_employe(empid):
    conn = conn.get_connection()

    query = f"delete from employe where empid = %s;"
    val = (empid, )
    cursor = conn.cursor()

    cursor.execute(query, val)

    conn.commit()

    cursor.close()
    conn.close()



delete_employe(10)






