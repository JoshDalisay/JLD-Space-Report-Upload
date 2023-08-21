import mysql.connector

def LastEntry():
    
    mydb = mysql.connector.connect(
        host="log-s8mo-2web",
        user="report_space",
        password="#Comp%Room3224!",
        database="space_report"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM space_report_table")
    myresult = mycursor.fetchall()
    #print(myresult)
    if not myresult:
        print("There is no data in the database")
    else:
        # Handle the non-empty result set
        lastDateUpdated = myresult[-1][1]


        newQuery = "SELECT * FROM space_report_table WHERE scan_date='{}'".format(lastDateUpdated)
        #print(newQuery)
        mycursor.execute(newQuery)
        newResult = mycursor.fetchall()
        for i in newResult:
            print(i)

    mydb.close()

