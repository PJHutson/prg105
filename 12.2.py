def get_sum(number):
    if len(number) == 0:            # if length is 0 then there is no sum
        return 0
    else:
        return number[0] + get_sum(number[1:])          # equation for sum

print(get_sum([1, 2, 3, 4, 5]))     # list to get the sumb
