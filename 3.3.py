# Classifying people by age
age = input("Please enter an age to be classified ")
Age = int(age)
if Age <= 1:
    print("This person would be an infant")
if 1 < Age < 13:
    print("This person would be a child")
if 13 < Age < 20:
    print("This person would be a teenage")
if Age >= 20:
    print("This person would be an adult")
