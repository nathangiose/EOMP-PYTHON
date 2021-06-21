# Nathan John Giose- Group2
# IMPORTING EVERYTHING FROM TKINTER


from tkinter import *


# CREATING THE GUI


root= Tk()
root.geometry("1600x800")
root.overrideredirect(True)
root.title("Powerball")
root.config(bg="#069edb")

# IMPORTING IMAGE


img = PhotoImage(file="powerball.png")
canvas = Canvas(root, width=391, height=129)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=480, y=280)


def play_nw():
   root.destroy()
   import Lotto_GUI

# SETTING THE TIMER FOR THE SPLASH SCREEN TO CLOSE


root.after(3000, play_nw)

mainloop()
