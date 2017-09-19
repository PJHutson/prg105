# set up the loop for calories burned
calories = 4.2          # calories burned per minute
for num in range(10, 31, 5):     # list range for the minutes
    print("The calories burned in ", num, " minutes are: ", calories * num)
