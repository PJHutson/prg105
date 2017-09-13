# Checking costs for packages based off of minutes
package = input("Please enter the letter for the package you purchased, A, B, or C: ")
minutes = input("Please enter then number of minutes you used: ")
Minutes = int(minutes)

if package == 'A':
    if Minutes <= 450:
        price = 39.99
        print("Your total cost is: ")
        print(price)
    else:
        price = 39.99 + .45*(Minutes-450)
        print("Your total cost is: ")
        print(price)
elif package == 'B':
    if Minutes <= 900:
        price = 59.99
        print("Your total cost is: ")
        print(price)
    else:
        price = 59.99 + .40 * (Minutes - 450)
        print("Your total cost is: ")
        print(price)
elif package == 'C':
    price = 69.99
    print("Your total cost is: ")
    print(price)
else:
    print("Please put in a correct type of package next time. ")
