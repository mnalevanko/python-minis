from tkinter import *
from calendar import *

def myCalendar(month, year):

    
    root = Tk()

    days = ['Pondelok', 'Utorok', 'Streda', 'Štvrtok', 'Piatok', 'Sobota', 'Nedeľa']
    for i in range(7):
        label = Label(root, text = days[i])
        label.grid(row = 0, column = i)

    weekday, numDays = monthrange(year, month)
    week = 1
    for i in range(1, numDays + 1):
        label = Label(root, text = str(i))
        label.grid(row = week, column = weekday)

        weekday += 1
        if weekday > 6:
            week += 1
            weekday = 0

    root.mainloop()

myCalendar(4, 2016)
    
