# Converting numbers between 1 and 7 into days of the week
number = input("Please enter a number from the range of 1 to 7 ")
Day = int(number)
if 1 <= Day <= 7:
    if Day == 1:
        print("Monday")
    if Day == 2:
        print("Tuesday")
    if Day == 3:
        print("Wednesday")
    if Day == 4:
        print("Thursday")
    if Day == 5:
        print("Friday")
    if Day == 6:
        print("Saturday")
    if Day == 7:
        print("Sunday")
else: print("Please enter a number between 1 and 7 and try again")
