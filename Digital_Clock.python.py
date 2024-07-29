#importing whole module
from tkinter import *
from tkinter.ttk import *

#importing strftime function to retriver system's time

from time import strftime

#Creating tkinter window
root = Tk()
root.title ('ShaliniS Clock')

#This function is used to display time on the label

def time() :
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000,time)


#Styling the label widget so that clock will looks more attractive
lbl = Label(root, font = ('calibri' , 100 , 'bold'),
            background = 'green',
            foreground = 'yellow')

#placing clock at the center of the tkinter window
lbl.pack(anchor = 'center')
time()
mainloop()
            
