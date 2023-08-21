import mysql.connector


def GetLastScanDate():
    mydb = mysql.connector.connect(
        host="log-s8mo-2web",
        user="report_space",
        password="#Comp%Room3224!",
        database="space_report"
    )

    thiscursor = mydb.cursor()
    thiscursor.execute("SELECT * FROM space_report_table ORDER BY scan_id DESC LIMIT 1")
    thisresult = thiscursor.fetchone()
    if not thisresult:
        print("There is no data in the database")
    else:
        # Handle the non-empty result set
        lastDate = thisresult[1]
        return(lastDate)
    

    mydb.close()

