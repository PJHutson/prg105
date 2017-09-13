# Converting numbers in to roman numerals
number = input("Please enter a number between 1 and 10 ")
Numeral = int(number)
if 1 <= Numeral <= 10:
    if Numeral == 1:
        print("I")
    if Numeral == 2:
        print("II")
    if Numeral == 3:
        print("IV")
    if Numeral == 5:
        print("V")
    if Numeral == 6:
        print("VI")
    if Numeral == 7:
        print("VII")
    if Numeral == 8:
        print("VIII")
    if Numeral == 9:
        print("IX")
    if Numeral == 10:
        print("X")
else: print("Please enter a number between 1 and 10 and try again.")
