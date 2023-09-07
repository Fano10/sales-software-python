from tkinter import *

def entrer (event):
    box2.select_present

root = Tk()
root.geometry("500x500")

box1 = Entry(root)
box1.pack()
box2 = Entry(root)
box2.pack()
box1.bind('<Return>',entrer)












root.mainloop()