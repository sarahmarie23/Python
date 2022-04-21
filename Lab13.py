# CS 232 - Spring 2022
# Lab 13

from tkinter import *

class Blow_it_up():
    def __init__(self, parent_window):
        self.frame = Frame(parent_window)
        self.frame.grid()
        self.string_out = StringVar()

        # Blow it up button
        self.blow_btn = Button(self.frame, font = ('Helvetica', 20))
        self.blow_btn.grid(row = 0, column = 2)
        self.blow_btn['text'] = "BLOW IT UP!"
        self.blow_btn['command'] = self.display

        # I'm done button
        self.done_btn = Button(self.frame, font = ('Helvetica', 20))
        self.done_btn.grid(row = 0, column = 3)
        self.done_btn['text'] = "I'm done"
        self.done_btn['command'] = self.frame.quit 

        # Labels
        self.header_lbl = Label(self.frame, font = ('Helvetica', 20))
        self.header_lbl.grid(row = 0, column = 0)
        self.header_lbl['text'] = "Enter word to blow up:"

        self.output_lbl = Label(self.frame, fg = 'red', font = ('Helvetica', 60))
        self.output_lbl.grid(row = 1, column = 0)
        self.output_lbl['textvariable'] = self.string_out

        # Text Boxes
        self.text_box = Entry(self.frame, fg = 'blue', font = ('Helvetica', 20))
        self.text_box.grid(row = 0, column = 1)
        self.text_box['width'] = 10

    def display(self):
        self.output = self.text_box.get()
        self.string_out.set(self.output)



def try_it():
    main_window = Tk()
    main_window.title("Blow It Up Lab")
    main_window.geometry("750x150")
    main_window['bg'] = "black"
    x = Blow_it_up(main_window)
    main_window.mainloop()
    main_window.destroy()
