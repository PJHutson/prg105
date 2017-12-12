import tkinter
import pickle


class Info:  # create class
    def __init__(self):
        self.main_window = tkinter.Tk()         # set up menu
        self.button_frame = tkinter.Frame(self.main_window)
        self.label_frame = tkinter.Frame(self.main_window)
        self.fname_frame = tkinter.Frame(self.main_window)            # creating frames
        self.lname_frame = tkinter.Frame(self.main_window)
        self.phonenum_frame = tkinter.Frame(self.main_window)
        self.email_frame = tkinter.Frame(self.main_window)
        self.address_frame = tkinter.Frame(self.main_window)
        self.result_frame = tkinter.Frame(self.main_window)
        self.fname_label = tkinter.Label(self.fname_frame, text="First Name")
        self.fname_entry = tkinter.Entry(self.fname_frame)        # set up frames for options
        self.fname_label.pack(side='left')
        self.fname_entry.pack(side='left')
        self.lname_label = tkinter.Label(self.lname_frame, text="Last Name")
        self.lname_entry = tkinter.Entry(self.lname_frame)
        self.lname_label.pack(side='left')
        self.lname_entry.pack(side='left')
        self.phonenum_label = tkinter.Label(self.phonenum_frame, text="Phone")
        self.phonenum_entry = tkinter.Entry(self.phonenum_frame)
        self.phonenum_label.pack(side='left')
        self.phonenum_entry.pack(side='left')
        self.email_label = tkinter.Label(self.email_frame, text="Email")
        self.email_entry = tkinter.Entry(self.email_frame)
        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')
        self.address_label = tkinter.Label(self.email_frame, text="Address")
        self.address_entry = tkinter.Entry(self.address_frame)
        self.address_label.pack(side='left')
        self.address_entry.pack(side='left')
        self.search_button = tkinter.Button(self.button_frame, text='search', command=self.search)
        self.search_button.pack(side='left')
        self.add_button = tkinter.Button(self.button_frame, text='add', command=self.add)
        self.add_button.pack(side='left')
        self.change_button = tkinter.Button(self.button_frame, text='change', command=self.change)
        self.change_button.pack(side='left')
        self.remove_button = tkinter.Button(self.button_frame, text='remove', command=self.remove)
        self.remove_button.pack(side='left')
        self.quit_button = tkinter.Button(self.button_frame, text='Exit', command=self.main_window.destroy)
        self.quit_button.pack(side='left')
        self.title = tkinter.Label(self.label_frame, text="Personal Info")
        self.title.pack(side="top")
        self.fname_frame.pack()
        self.lname_frame.pack()
        self.phonenum_frame.pack()
        self.email_frame.pack()
        self.address_frame.pack()
        self.title.pack()
        self.label_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        self.First_name = tkinter.StringVar()
        self.First_name = self.fname_entry
        self.Last_name = tkinter.StringVar()
        self.Last_name = self.lname_entry
        self.Phone = tkinter.StringVar()
        self.Phone = self.phonenum_entry
        self.Email_address = tkinter.StringVar()
        self.Email_address = self.email_entry
        self.Street_address = tkinter.StringVar()
        self.Street_address = self.address_entry
        self.searchresult = tkinter.StringVar
        self.search_result = tkinter.Label(self.result_frame, textvariable=self.searchresult)
        self.search_result.pack()
        self.add_result = tkinter.StringVar
        self.addresult = tkinter.Label(self.result_frame, textvariable=self.add_result)
        self.addresult.pack()
        self.removeresult = tkinter.StringVar
        self.remove_result = tkinter.Label(self.result_frame, textvariable=self.removeresult)
        self.remove_result.pack()
        self.changeresult = tkinter.StringVar
        self.change_result = tkinter.Label(self.result_frame, textvariable=self.changeresult)
        self.change_result.pack()

        tkinter.mainloop()

    def search(self):
        try:  # function to search the list
            input_file = open("Contacts.py", 'rb')
            contacts = pickle.load(input_file)
        except (FileNotFoundError, IOError):
            contacts = {}
        contact1 = [self.First_name, self.Last_name, self.Phone, self.Email_address, self.Street_address]
        contactperson = tuple(contact1)
        if contactperson in contacts:
            self.searchresult = "Heres the contact"
        else:
            self.searchresult = "Cant find the contact"
        save_file = open('Contacts.dat', 'wb')
        pickle.dump(contacts, save_file)
        save_file.close()

    def add(self):
        try:  # function to add to the list
            input_file = open("Contacts.py", 'rb')
            contacts = pickle.load(input_file)
        except (FileNotFoundError, IOError):
            contacts = {}
        contact2 = [self.First_name, self.Last_name, self.Phone, self.Email_address, self.Street_address]
        contactperson2 = tuple(contact2)
        if contactperson2 not in contacts:
            self.addresult = "You have added the contact"
        else:
            self.addresult = "That contact already exists"
        save_file = open('Contacts.dat', 'wb')
        pickle.dump(contacts, save_file)
        save_file.close()

    def change(self):
        try:  # function to change info in the list
            input_file = open("Contacts.py", 'rb')
            contacts = pickle.load(input_file)
        except (FileNotFoundError, IOError):
            contacts = {}
        contact3 = [self.First_name, self.Last_name, self.Phone, self.Email_address, self.Street_address]
        contactperson3 = tuple(contact3)
        if contactperson3 in contacts:
            del contacts[contactperson3]
            self.changeresult = "You have changed the contact"
        else:
            self.changeresult = "That contact doesnt even exist"
        save_file = open('Contacts.dat', 'wb')
        pickle.dump(contacts, save_file)
        save_file.close()

    def remove(self):
        try:  # function to remove the function
            input_file = open("Contacts.py", 'rb')
            contacts = pickle.load(input_file)
        save_file = open('Contacts.dat', 'wb')
        pickle.dump(contacts, save_file)
        save_file.close()

Info()
