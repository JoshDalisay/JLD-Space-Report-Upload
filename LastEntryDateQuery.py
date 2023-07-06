import mysql.connector

def LastEntry():
    
    mydb = mysql.connector.connect(
        host="log-s8mo-2web",
        user="jdalis5n",
        password="South567456843!",
        database="space_report"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM space_report_table")
    myresult = mycursor.fetchall()
    #print(myresult)
    lastDateUpdated = myresult[-1][1]


    newQuery = "SELECT * FROM space_report_table WHERE scan_date='{}'".format(lastDateUpdated)
    #print(newQuery)
    mycursor.execute(newQuery)
    newResult = mycursor.fetchall()
    for i in newResult:
        print(i)

    mydb.close()

