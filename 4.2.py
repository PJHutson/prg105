Days = int(input("Please enter the amount of days worked "))        # make the days worked an integer
Pay = 0.01          # initial pay
pennies = 0
print("Days worked | Amount Earned that Day")           # titles for table columns
print("--------------------------------------")
for day in range(1, Days + 1):
    print('\t', day, '\t', "| $ ", Pay)         # print the days with their pay
    Pay = 2 * Pay
print("Total pay", Pay)     # Total pay
