# worker efficiency is determined on the basis of the time required

time_taken_by_worker = float(input("Enter time taken in hours to complete a job: "))

if (time_taken_by_worker >= 2) and (time_taken_by_worker <= 3):
    print("highly efficient")
elif (time_taken_by_worker >3) and (time_taken_by_worker <= 4):
    print("Please try to improve your speed.")
elif (time_taken_by_worker > 4) and (time_taken_by_worker <= 5):
    print("You are given a training to improve your speed.")
elif (time_taken_by_worker > 5):
    print("Sorry! You are fired from the company.")            