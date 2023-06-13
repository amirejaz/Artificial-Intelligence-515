# CONTROL STRUCTURES IF ELSE ELIF:
# eg 01
# a = int(input("Enter a number and I'll get its square root: "))
# if (a> 0):
#     print("The number you entered is greater than 0, so I can calculate it!")
#     root = a ** (1/2)
#     print("The square root of ", a ," is: ", root)
# if (a <= 0):
#     print("I can't calculate the square root of a negative number!")
# print("Thanks for the input!")


# eg 02
# a = int(input('')) # the variable is initialized with a value of 0

# if (a == 1): # if the value is 1, we change its value to 0
#     a=0 
# if (a == 0): # if the value is 0, we change its value to 1
#     a=1
# if (a>2 or a<0):
#     print("You have entered number between")
# print(a)

# eg 3
# a = int(input("Enter a number between 10-20: "))
# if a >= 10 and a <= 20:
#     print("The condition has been met.")
# else:
#     print("You did it wrong.")

# eg 4
a = int(input("Enter a number between 10-20 or 30-40: "))
if (a >= 10 and a <= 20) or (a >= 30 and a <= 40):
    print("The condition has been met.")
else:
    print("You did it wrong.")
