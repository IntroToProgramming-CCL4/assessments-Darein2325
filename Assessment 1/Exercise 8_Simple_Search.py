# Exercise 8 Simple Search

#Shows the list of names to search through
print(["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"])

#Creates a loop until the correct name is found
while True:
         #A list of the names
         names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
         #Ask the user to enter a name 
         search =input("Enter a name:")
         #Checks if given name matches "Sam" (4)
         if search in (names[4]):
          #If it's correct it displays a success message and breaks the loop
          print("You've found the name!")
          break
         #If the name entered is in the list but is not "Sam", inform the user to try again
         elif search in names :
          print("The given name is in the list but it's not the one looking for. Please try again.")
         else:
         #If the name entered is not in the list, inform the user to try again
          print("The given name is not on the list. Try again and choose from the list.")
          