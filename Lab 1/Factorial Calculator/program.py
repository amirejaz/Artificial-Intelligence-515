# Python Program that calculates factorial of a number
print("Welcome to the Factorial Calculator!")
num = 5
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Using while loop
while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num >= 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a valid number.")

result = factorial(num)
print("The factorial of" ,num ," is ", result,".")
