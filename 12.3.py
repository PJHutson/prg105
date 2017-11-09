def power(x, y):
    if y == 0:      # anything to the 0 is 1
        return 1
    elif y >= 1:
        return x * power(x, y-1)        # equation for the power

print(power(3, 5))      # solve 3^5
