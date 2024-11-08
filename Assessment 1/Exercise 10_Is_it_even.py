# Exercise 10: Is it even?

#Ask the user to enter a number can be either a float(a decimal)
number = float(input("Enter a number: "))

#Check if the number is even by dividing by 2 is 0
if number % 2 == 0:
    print("Even")
else:
    #f remainder is not 0, it's an odd number
    print("Odd")