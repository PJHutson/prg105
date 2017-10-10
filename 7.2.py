def main():
    import random       # randomize
    random_list = []
    for i in range(20):            # set it to 20 numbers
        random_list.append(random.randrange(1, 101, 1))               # give the bounds
    return random_list


def user():                 # set up the user input
    count = 0
    try:
        while count == 0:
            user_value = int(input("Please enter a number between 1 and 100: "))
            if 1 <= user_value <= 100:              # make sure user input is in the range
                count += 1
                return user_value
            else:
                print("\nThat is not a valid number")
    except TypeError:
        print("Sorry, there was an error with your answer")
    except ValueError:
        print("Sorry, there was an error with your answer")


def display(num, nums):             # set up display
    index = 0
    count = 0
    while index < 20:                   # comparison, if user input is lower than numbers in list
        if int(nums[index]) > num:
            pri = nums[index]
            print(pri)
        else:
            count += 1
        index += 1
    if count == 20:
        print("None of the numbers in the list are greater than yours")             # show you have the greatest number

display(user(), main())
