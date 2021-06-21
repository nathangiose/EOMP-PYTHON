# Nathan John Giose- Group2

from tkinter import *
import random
from tkinter import messagebox


root = Tk()
root.geometry("500x500")
root.title("LOTTERY GAME")
root.config(bg='#069edb')
root.resizable(0, 0)

# INSERT IMAGE


img = PhotoImage(file="powerball.png")
canvas = Canvas(root, width=391, height=129)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=55, y=0)

# INSERT NUMBERS


root.mainloop()
