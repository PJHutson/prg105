def calc_average():
    total = 0       # initial total is 0
    test_1 = input("Please enter your first test grade: ")      # add in first test grade
    while not test_1.isdigit():         # check for errors
        test_1 = input("Please re-enter your grade with proper numbers: ")
    test_one = int(test_1)
    total += test_one
    test_2 = input("Please enter your second test grade: ")         # add in second grade
    while not test_2.isdigit():         # test for errors
        test_2 = input("Please re-enter your grade with proper numbers: ")
    test_two = int(test_2)
    total += test_two
    test_3 = input("Please enter your third grade: ")           # add in third grade
    while not test_3.isdigit():         # test for errors
        test_3 = input("Please re-enter your grade with proper numbers: ")
    test_three = int(test_3)
    total += test_three
    test_4 = input("Please enter your fourth test grade: ")         # add in fourth grade
    while not test_4.isdigit():         # test for errors
        test_4 = input("Please re-enter your grade with proper numbers: ")
    test_four = int(test_4)
    total += test_four
    test_5 = input("Please enter your fifth test grade: ")      # add in fifth grade
    while not test_5.isdigit():         # test for errors
        test_5 = input("Please re-enter your grade with proper numbers: ")
    test_five = int(test_5)
    total += test_five
    return total        # find the total


def determine_grade(num):
    average = int(num / 5)          # divide total by 5 for the average grade
    print("The average grade was ", average)
    if average >= 90:           # above 90 is an A etc for following grades
        print("The final grade was an A")
    elif 90 > average >= 80:
        print("The final grade was a B")
    elif 80 > average >= 70:
        print("The final grade was a C")
    elif 70 > average >= 60:
        print("The final grade was a D")
    else:
        print("The final grade was a F")

determine_grade(calc_average())     # output
