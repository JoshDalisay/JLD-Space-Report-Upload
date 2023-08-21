import mysql.connector
import os
import ScanDateChecker
import ResultsFileReader 
import LastEntryDateQuery as le
from DateCheckerQuery import GetLastScanDate as lsd
from datetime import date, datetime, timedelta
import re
import time
from time import sleep
from tqdm import tqdm


mydb = mysql.connector.connect(
    host="log-s8mo-2web",
    user="report_space",
    password="#Comp%Room3224!",
    database="space_report"
)



cursor = mydb.cursor()

workstation_name = ""
storage_left = ""


#Get today's date
today = datetime.now().date()
today = str(today)

#Get the date of the scan output file. Effectively the date scanned.
ResultsFilePath = r'\\log-s8mo-1fs\groups\IT Support\Windows 10\Scripts\results.txt'
ti_m = os.path.getmtime(ResultsFilePath)
m_ti = time.ctime(ti_m)
t_obj = time.strptime(m_ti)
T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
match = re.search(r'\d{4}-\d{2}-\d{2}', T_stamp)
reportDate = (match.group())

#print(f"The file located at the path {ResultsFilePath} was last modified at {T_stamp}")

#Read the information inside the scanned output file
TextOutputRead = ResultsFileReader.ResultsReader()
#Gets the date of the last item scanned into the database.
last_date_entry = str(lsd())


print("Today's date: " + today)
print("\n------------------------------------")
print("\nReport date: " + reportDate)
print("\nLast date in database: " + last_date_entry + "\n")
if len(TextOutputRead) > 0:
    DateCheck = ScanDateChecker.CheckScanDate(reportDate, last_date_entry)
else:
    DateCheck = False



if DateCheck == True and len(TextOutputRead) > 0:
    for item in TextOutputRead:
        workstation_name = item[0]
        storage_left = item[1]

        #This removes the GB from storage left
        non_decimal = re.compile(r'[^\d.]+')
        storage_left = float(non_decimal.sub('', storage_left))

        sql = 'INSERT INTO space_report_table (scan_date, workstation_name, storage_left) VALUES (%s, %s, %s);'
        val = (reportDate, workstation_name, storage_left)
        cursor.execute(sql, val)
        
        print("\nItem to insert: " + str(val))
        print("Do you want to commit? y or n\n")
        while True:
            try:
                user_input = input("Enter 'y' or 'n': ")
                if user_input not in ['y', 'n']:
                    raise ValueError("Invalid input. Please enter 'y' or 'n'.")
                else: 
                    if user_input.lower() == "y":
                        #Reduce sleep value to increase "performance"
                        print("\nCommitting " + str(val) + " to MySQL Database...")
                        for t in tqdm(range(100)):
                            sleep(0.009)
                        mydb.commit()
                    else:
                        print("\nNot Committing...")
                        print(str(val))
                    
                break
            except ValueError as e:
                print(e)
        break
        
        
        
        #This statement is the one that initializes the insert into the table. 
        #Do not use more than once a day to avoid duplicate entries
        
    print("\nJob completed.")
#print("affected rows = {}".format(cursor.rowcount))

print("\nLatest Entries in database: ")
le.LastEntry()

mydb.close()

programPause = input("\nPress the <ENTER> key to continue...")