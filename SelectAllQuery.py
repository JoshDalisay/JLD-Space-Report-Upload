import mysql.connector

mydb = mysql.connector.connect(
    host="log-s8mo-2web",
    user="jdalis5n",
    password="South567456843!",
    database="space_report"
)

# FIND A TRUNCATE TABLE STATEMENT 
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM space_report_table")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
mydb.close()


