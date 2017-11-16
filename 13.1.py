import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()         # main window
        self.name_value = tkinter.StringVar()       # creating string variables for display
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()
        self.info_frame = tkinter.Frame(self.main_window)       # making 2 frames
        self.button_frame = tkinter.Frame(self.main_window)
        self.name_label = tkinter.Label(self.info_frame, textvariable=self.name_value)      # creating label widgets for variables
        self.street_label = tkinter.Label(self.info_frame, textvariable=self.street_value)
        self.csz_label = tkinter.Label(self.info_frame, textvariable=self.csz_value)
        self.name_label.pack()          # packing all the labels
        self.street_label.pack()
        self.csz_label.pack()
        self.show_info_button = tkinter.Button(self.button_frame, text='Show Info', command=self.show)          # creating button widgets
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.show_info_button.pack(side='left')             # packing the buttons
        self.quit_button.pack(side='right')
        self.info_frame.pack()          # pack the frames
        self.button_frame.pack()
        tkinter.mainloop()          # enter main loop

    def show(self):         # call back
        self.name_value.set('Paul Hutson')
        self.street_value.set('6802 Meadow Dr')
        self.csz_value.set('Crystal Lake, IL 60012')


my_gui = MyGui()            # create an instance of the class
