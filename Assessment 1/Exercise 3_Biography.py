#Exercise 3 Biography

#Asks the user to enter their full name 
name = input("Enter your full name: ")

#Asks the user to enter their hometown
hometown = input("Enter your hometown: ")

while True: #Makes a loop so that the user would put a valid integer
     age_input = input("Enter your age: ")  #Asks the user to enter their age
     if age_input.isdigit(): #Checks the string if it's a valid integer
            #A variable   
            age = int(age_input)
            break #Exits the loop since a valid integer has been given
     else:
       print("Invalid age, please try again.")  #Notifies the user that the given is invalid
       
#A dictionary to store the user's information
user_info = { "name": name,"hometown": hometown,"age": age}

#Displays all of the given information of the user and stores it in the dictionary provided
print(f"\nname: {user_info['name']} hometown: {user_info['hometown']} age: {user_info['age']}")