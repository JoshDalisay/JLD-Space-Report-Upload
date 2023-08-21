import mysql.connector

mydb = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

# FIND A TRUNCATE TABLE STATEMENT 
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM space_report_table")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
mydb.close()


