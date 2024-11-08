#Exercise 5: Days of the Month

#A dictionary to store the number of days in each month and the order of months
days_in_a_month = {1: 31,  2: 28,  3: 31,  4: 30,  5: 31,  6: 30,   7: 31,   8: 31,   9: 30,   10: 31,   11: 30, 12: 31  }

#Ask the user to enter a month number
month = int(input("Enter a month number (1-12): "))  

#Check if given number is valid between 1 and 12
if month >= 1 and month <= 12:
     #Checks if it's Febuary which month 2
     if month == 2:  
        # Febuary Leap year formula
        year = int(input("Enter the year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            #Displays if it's a leap year
            print(f"February {year} has 29 days and is a leap year.")
        else:
             #Displays if it's a non-leap year
            print(f"February {year} has 28 days.")
      #Displays the days in other given months from the dictionary
     else:
      print(f"The month {month} has {days_in_a_month[month]} days.")
else:
    #If the given number is not on the list
    print("The month number chosen is not on the list. Please pick a number from 1-12.")