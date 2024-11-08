#Exercise 6: Brute Force Attack

#Places a maximum number of attempts
Tries= 5

#
attempts=0

#Makes a loop that allows the user to put the password until the maximum attempts
while attempts < Tries:
    password = input("Please enter the password: ") #Ask the user to enter a password
    if password =="12345": #Check's if given password is correct
     print("GOODJOB! YOU GOT IT CORREECT !!") #Tells the user the their given password is correct and breaks loop
     break
    #If password is incorrect, increase the number of attempts
    else:
      attempts += 1
      remaining_attempts = Tries- attempts #Calculates the remaining attempts 
      if  remaining_attempts>0: #Tells the user their passwrod is incorrect and their remaining attempts
       print(f"The passsword is incorrect you have {remaining_attempts} more attempts.")
      else:
       #Informs the user that they have reached the maximum attempts
       print("you have reached the maximum attempts.")
    
  