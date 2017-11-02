def main():
    input_file = open('BoyNames.txt', 'r')
    boy_names = input_file.readlines()

    input_file.close()

    index = 0
    while index < len(boy_names):
        boy_names[index] = boy_names[index].rstrip('\n')
        index += 1

    boy = input("Please enter a boys name: ")
    print(boy_names)

    if boy in boy_names:
        print("Yes", boy, "is in the list!")
    else:
        print("No", boy, "is not in the list")


    input_file2 = open('GirlNames.txt')
    girl_names = input_file2.readlines()
    input_file2.close()
    index = 0
    while index < len(girl_names):
        girl_names[index] = girl_names[index].rstrip('\n')
        index += 1

    girl = input("Please enter a girls name: ")
    print(girl_names)

    if girl in girl_names:
        print("Yes that is in the list")
    else:
        print("No that is not in the list")

main()
