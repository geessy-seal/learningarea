""""
Write an if statement that assigns 20 to the variable y,
and assigns 40 to the variable z if the variable x is
greater than 100.
"""
x = int(input("enter any intreger: "))
if x > 100:
    y = 20
    z = 40

"""
Write a program that reads in a positive integer n from
the user and then prints whether n is even or odd.
Hint: An even number is a multiple of 2. Any multiple of
2 leaves a remainder of zero when divided by 2.
An example run of the program is shown below. 
"""

num = int(input("enter positive integer: "))
if num % 2 == 0:
    print(num, " is even")

else:
    print(num, " is ood")
"""
Exercise: Maximum Number
Write a program that asks the user to enter 3 integers.
The program should display the maximum number.
"""
num1 = int(input("enter an integer: "))
num2 = int(input("enter an integer: "))
num3 = int(input("enter an integer: "))

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num3:
    print(num2)
else:
    print(num3)

#---------------------------------------------------------------------
# Ask the user for three integers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Initialize a variable to hold the largest value
# We start by assuming the first number is the largest
maximum = num1

# Compare the current maximum with the second number
if num2 > maximum:
    maximum = num2

# Compare the current maximum with the third number
if num3 > maximum:
    maximum = num3

# Display the result
print(f"The maximum number is: {maximum}")

