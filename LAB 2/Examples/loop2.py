# Take collection of number input from user. Print the total positive and negative number
pcount = 0
ncount = 0
count = int(input("how many numbers you want? "))
i = 1
while(i<=count):
    num = int(input("Enter number: "))
    if (num >= 0):
        pcount += 1
    else:
        ncount += 1
    i+=1
print("positive: ", pcount)
print("negative: ", ncount)