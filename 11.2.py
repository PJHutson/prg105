import employee          # import class

name = input('Please enter your name, first then last: ')
number = input('Please enter your employee number: ')
shift = input('Please enter your shift number(1 = First shift, 2 = Second shift, 3 = Third shift.): ')
hourlypayrate = input('Please enter your hourly pay rate: ')

my_Employee = employee.ProductionWorker(name, number, shift, hourlypayrate)

print('Employee Information')
print('Name:', my_Employee.get_name())
print('Employee Number:', my_Employee.get_number())
print('Hourly Pay Rate:', my_Employee.get_hourlypayrate())
