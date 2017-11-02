import pickle


LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    try:
        input_file = open("customer.file.dat", 'rb')
        customers = pickle.load(input_file)
    except (FileNotFoundError, IOError):
        print("File not found, there was an error. Please add a customer and quit.")
        customers = {}

    choice = 0

    while choice != QUIT:
        choice = menu()
        if choice == LOOK_UP:
            look_up(customers)
        elif choice == ADD:
            add(customers)
        elif choice == CHANGE:
            change(customers)
        elif choice == DELETE:
            delete(customers)
        elif choice == QUIT:
            save(customers)


def menu():
    print()
    print("Customer phone search")
    print("---------------------")
    print("1. Look up a customer")
    print("2. Add a customer")
    print("3. Change a number")
    print("4. Delete a number")
    print("5. Quit the program\n")

    choice = int(input("Please enter the number for your choice: "))
    if choice < 1 or choice > 5:
        print("Please enter a valid number")
    else:
        return choice


def look_up(customers):
    name = input("Please enter a name")
    print(customers.get(name, 'Not found'))


def add(customers):
    name = input("Please enter a customer's name: ")
    phone = input("Please enter the phone number")
    if name not in customers:
        customers[name] = phone
    else:
        print("That person/number already exists")


def change(customers):
    name = input("Please enter the customer's name: ")
    if name in customers:
        phone = input("Please enter the new phone number.")
        customers[name] = phone
    else:
        print("That customer can not be found.")


def delete(customers):
    name = input("Please enter the customer's name: ")
    if name in customers:
        del customers[name]
    else:
        print("That customer can not be found.")


def save(customers):
    print("The data has been successfully saved.")
    save_file = open('customer.file.dat', 'wb')
    pickle.dump(customers, save_file)
    save_file.close()


main()
