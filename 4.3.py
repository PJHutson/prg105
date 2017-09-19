# Nested loops to find the average rainfall
rainfall = 0
years = int(input("Please enter the number of years"))      # convert years to integer
for year in range(1, years + 1):        # set loops for the years
    for month in range(1, 13):          # set inner loops for months
        rainfallpermonth = int(input("Please input the inches of rain this month"))
        rainfall += rainfallpermonth        # Total rainfall
print("The number of months is", years * 12)
print("The total inches of rainfall is", rainfall)
print("The average rainfall per month is", rainfall / (years * 12))
