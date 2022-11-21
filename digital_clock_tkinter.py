from tkinter import *
from turtle import bgcolor
from datetime import datetime
from time import time


#Colors Used
bc = "#232423"
fc = "#00e331"

#Window Setup
window = Tk()
window.title("Digital Clock")
window.geometry('350x150')
window.resizable(width=False, height=False)
window.configure(bg=bc)


#Clock Functionality

def clock():
    time = datetime.now()
    hour = time.strftime( '%H : %M : %S')
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%B")
    year = time.strftime("%Y")
    l1.configure(text=hour)
    l1.after(200, clock)
    l2.configure(text=weekday + " " + str(month) + " / " + str(day) + " / " + str(year))
    print(clock)

l1 = Label(window, text = "%H %M %S", font=('Times 60'), bg = bc, fg = fc)
l1.grid(row = 0, column = 0, padx=30, pady=10, sticky = NW)

l2 = Label(window, text = "Monday 11/21/2012", font=('Times 20'), bg = bc, fg = fc)
l2.grid(row = 1, column = 0, sticky = NW, padx=40)

clock()
    
window.mainloop()
