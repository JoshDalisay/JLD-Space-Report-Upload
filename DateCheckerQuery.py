import mysql.connector


def GetLastScanDate():
    mydb = mysql.connector.connect(
        host="log-s8mo-2web",
        user="jdalis5n",
        password="South567456843!",
        database="space_report"
    )

    thiscursor = mydb.cursor()
    thiscursor.execute("SELECT * FROM space_report_table ORDER BY scan_id DESC LIMIT 1")
    thisresult = thiscursor.fetchone()
    lastDate = thisresult[1]
    return(lastDate)

    mydb.close()

