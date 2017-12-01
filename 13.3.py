import tkinter


class GUI:          # creating initial class for the GUI

    def __init__(self):
        self.main_window = tkinter.Tk()             # setting the menu
        self.gallons_frame = tkinter.Frame(self.main_window)            # creating frames
        self.miles_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.mpg_frame = tkinter.Frame(self.main_window)
        self.gallons_label = tkinter.Label(self.gallons_frame, text="Please enter the number of gallons in your tank: ")  # getting gallons
        self.gallons_entry = tkinter.Entry(self.gallons_frame)
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')
        self.miles_label = tkinter.Label(self.miles_frame, text="Please enter the miles you can travel on a full tank: ")      # getting miles
        self.miles_entry = tkinter.Entry(self.miles_frame)
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')
        self.result_label = tkinter.Label(self.mpg_frame, text='mpg =')
        self.mpg = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mpg_frame, textvariable=self.mpg)
        self.result_label.pack(side='left')
        self.mpg_label.pack(side='left')
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate miles per gallon', command=self.calc_gallons)      # on click perform that function
        self.quit_button = tkinter.Button(self.button_frame, text='Exit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='right')
        self.gallons_frame.pack()               # packing all the info
        self.miles_frame.pack()
        self.button_frame.pack()
        self.mpg_frame.pack()
        tkinter.mainloop()

    def calc_gallons(self):             # function to do the actual calculations
        self.gallons = float(self.gallons_entry.get())
        self.miles = float(self.miles_entry.get())
        print(self.gallons, self.miles)
        self.mpg = self.miles / self.gallons
        self.result_label['text'] = "'mpg = '{:0.2f}".format(self.mpg)

gas_miles = GUI()
