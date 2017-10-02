infile = open("numbers.txt")            # open the file

total = 0               # set initial total and lines to 0
lines = 0
try:
    for line in infile:                 # set up the math to calculate total and lines
        total += float(line)
        lines = lines + 1
except IOError:
    print("Sorry, an error has occurred and the file cannot be read")
except ValueError:
    print("The given values are invalid")

print("There were", lines, "numbers read in this file")
print("The average was", round((total/lines), 2))       # print the average

infile.close()
