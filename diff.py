# Write a Python program to calculate the difference between a given number and 17.
#  If the number is greater than 17, return twice the absolute difference.


# the number 17
number1=17
# prompt for the user to input the number
number2=int(input("enter any number: "))
# validate the user input
if number2>number1:
    print("the difference is: ",2*(number2-number1))
else:
    print("the difference is: ",number2-number1)