class Data:
    def __init__(self, address=None, age=None, phone_number=None, name=None):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    def __str__(self):
        summary = self.__name + " is " + self.__age + " and "
        if self.__address is not None:
            summary += "lives at " + self.__address
        summary += "."
        if self.__phone_number is not None:
            summary += " and has a phone number of " + self.__phone_number
        summary += "."
        return summary


person2 = Data("6802 Meadow Dr", "53", "815-690-0253", "Dean")
print(person2)

person3 = Data("6802 Meadow Dr", "51", "815-690-3777", "Lisa")
print(person3)

person4 = Data("6802 Meadow Dr", "24", "815-375-7676", "Britany")
print(person4)
