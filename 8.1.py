def main():

    name = input('Please type your full name, including your middle name. ')
    name_list = name.split()

    for part in name_list:
        print(part[0].upper() + ". ", end="")
    print()

main()
