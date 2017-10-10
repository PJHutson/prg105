def main():
    num_months = 12     # months for the year
    index = 0
    new_rainfall = [0] * num_months
    total_rainfall = 0

    print("Rainfall per month, please enter the rainfall for the month")
    while index < num_months:
        print('For month', index + 1, ': ')     # start at 1
        new_rainfall[index] = int(input())
        index += 1

    count = 0
    while count < num_months:           # set up the count for total
        print('The month had', new_rainfall[count], 'rainfall')
        total_rainfall += new_rainfall[count]           # all the new together equals the total
        count += 1
    average = total_rainfall / num_months           # average for the year

    print('There was ', total_rainfall, 'this year.')
    print('For an average of ', average, 'rainfall each month')
    print('The least rainfall in a month was: ', min(new_rainfall))
    print('The most rainfall in a month was: ', max(new_rainfall))

main()
