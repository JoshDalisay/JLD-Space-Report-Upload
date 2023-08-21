def CheckScanDate(todays_date, last_date_entry):
    #print(todays_date,last_date_entry)
    #print(todays_date == last_date_entry)
    if todays_date != last_date_entry:
        print("\nThese dates are not the same. Good to commit.")
        return True
    else: 
        print("\nThese dates are the same. Commit NOT CLEARED")
        print("\nWould you like to force a commit anyway?")
        while True:
            try:
                user_input = input("Enter 'y' or 'n': ")
                if user_input not in ['y', 'n']:
                    raise ValueError("Invalid input. Please enter 'y' or 'n'.")
                else: 
                    if user_input.lower() == 'y':
                        return True
                    else:
                        return False
                break
            except ValueError as e:
                print(e)
        return False