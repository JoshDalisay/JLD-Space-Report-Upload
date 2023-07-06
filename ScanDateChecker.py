def CheckScanDate(todays_date, last_date_entry):
    #print(todays_date,last_date_entry)
    #print(todays_date == last_date_entry)
    if todays_date != last_date_entry:
        print("\nThese dates are not the same. Approved to commit.")
        return True
    else: 
        print("\nThese dates are the same. Not commiting.")
        return False