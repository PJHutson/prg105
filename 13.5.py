import tkinter


class Coffee:  # create class
    def __init__(self):
        self.total = 0          # set total initially to 0
        self.total_cost = int(self.total)
        self.main_window = tkinter.Tk()         # set up menu
        self.button_frame = tkinter.Frame(self.main_window)
        self.label_frame = tkinter.Frame(self.main_window)
        self.frappuccino_button = tkinter.Button(self.button_frame, text='frappuccino', command=self.frappuccino_coffee)        # set up frames for options
        self.decaf_button = tkinter.Button(self.button_frame, text='decaf', command=self.decaf_coffee)
        self.french_roast_button = tkinter.Button(self.button_frame, text='french roast', command=self.french_roast_coffee)
        self.medium_roast_button = tkinter.Button(self.button_frame, text='medium roast', command=self.medium_roast_coffee)
        self.mocha_button = tkinter.Button(self.button_frame, text='mocha', command=self.mocha_coffee)
        self.small_button = tkinter.Button(self.button_frame, text='small', command=self.small_coffee)
        self.medium_button = tkinter.Button(self.button_frame, text='medium', command=self.medium_coffee)
        self.large_button = tkinter.Button(self.button_frame, text='large', command=self.large_coffee)
        self.quit_button = tkinter.Button(self.button_frame, text='Exit', command=self.main_window.destroy)
        self.total_label = tkinter.Label(self.label_frame, text='total cost=')
        self.title = tkinter.Label(self.label_frame, text="Coffee")
        self.frappuccino_button.pack(side='left')       # pack the options on menu
        self.decaf_button.pack(side='left')
        self.french_roast_button.pack(side='left')
        self.medium_roast_button.pack(side='left')
        self.mocha_button.pack(side='left')
        self.small_button.pack(side='left')
        self.medium_button.pack(side='left')
        self.large_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.title.pack()
        self.label_frame.pack()
        self.total_label.pack()
        self.button_frame.pack()
        tkinter.mainloop()
    # set up functions for each option to add to the total
    def small_coffee(self):
        self.total_cost += 2
        self.total_label['text'] = "'total cost = '{:0.2f}".format(self.total_cost)

    def medium_coffee(self):
        self.total_cost += 3
        self.total_label['text'] = "'total cost = '{:0.2f}".format(self.total_cost)

    def large_coffee(self):
        self.total_cost += 4
        self.total_label['text'] = "'total cost = '{:0.2f}".format(self.total_cost)

    def decaf_coffee(self):
        self.total_cost += 2.5
        self.total_label['text'] = "'total cost = '{:0.2f}".format(self.total_cost)

    def frappuccino_coffee(self):
        self.total_cost += 5
        self.total_label['text'] = "'total cost = '{:0.2f}".format(self.total_cost)

    def french_roast_coffee(self):
        self.total_cost += 3
        self.total_label['text'] = "'total cost = '{:0.2f}".format(self.total_cost)

    def medium_roast_coffee(self):
        self.total_cost += 3
        self.total_label['text'] = "'total cost = '{:0.2f}".format(self.total_cost)

    def mocha_coffee(self):
        self.total_cost += 5
        self.total_label['text'] = "'total cost = '{:0.2f}".format(self.total_cost)

Coffee()
