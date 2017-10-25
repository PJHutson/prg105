def main():         # setup
    print("Calculate for the monthly expenses")
    total = 0
    loan = input("Please enter how much you pay a month for a loan: ")      # ask for loans
    while not loan.isdigit():           # check for errors
        loan = input("There was an error, please enter your monthly loan again with proper numbers: ")
    loan_1 = int(loan)
    total += loan_1         # add loan to total
    insurance = input("Please enter how much you pay for insurance a month: ")      # ask for insurance
    while not insurance.isdigit():          # test for errors
        insurance = input("There was an error, please enter your monthly pay for insurance again with proper numbers: ")
    insurance_1 = int(insurance)
    total += insurance_1
    gas = input("Please enter how much you spend on gas a month: ")         # ask for gas
    while not gas.isdigit():            # check for errors
        gas = input("There was an error, please enter how much you pay for gas a month again with proper numbers: ")
    gas_1 = int(gas)
    total += gas_1
    maintenance = input("Please enter how much you pay on maintenance a month: ")           # ask for maintenance
    while not maintenance.isdigit():            # check for errors
        maintenance = input("There was an error, please enter how uch you pay for maintenance a month again with proper numbers: ")
    maintenance_1 = int(maintenance)
    total += maintenance_1

    print("You are spending an average of", (format(total, ',.2f')), "dollars")
    return total            # setting up total for the month


def second(num):        # yearly cost
    print("The approximate amount you will spend a year is", (format((num * 12), ',.2f')), "dollars")

second(main())
