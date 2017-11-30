import tkinter


class MyGui:
    def _init__(self):
        self.main_window = tkinter.Tk()
        self.mpg = tkinter.StringVar()
        self.gallons = tkinter.IntVar()
        self.miles = tkinter.IntVar()
        self.gallons_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.mpg_frame = tkinter.Frame(self.main_window)
        self.gallons_label = tkinter.Label(self.gallons, text='Please enter the number of gallons in a full tank: ')
        self.gallons_entry = tkinter.Entry(self.gallons_frame)
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')
        self.miles_label = tkinter.Label(self.miles, text='Please enter the number of miles you can travel on a full tank: ')
        self.miles_entry = tkinter.Entry(self.miles_frame)
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')
        self.answer_label = tkinter.Label(self.mpg_frame, text='MPG=')
        self.mpg_label = tkinter.Label(self.mpg_frame, textvariable=self.mpg)
        self.result_label.pack(side='left')
        self.mpg_label.pack(side='left')
        self.calc_button = tkinter.Button(self_button_frame, text)

my_gui = MyGui
