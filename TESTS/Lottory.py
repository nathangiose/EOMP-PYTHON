import random
from tkinter import  *

def Lotto_No():
    q = random.randint(1, 49);
    w = random.randint(1, 49);
    e = random.randint(1, 49);
    r = random.randint(1, 49);
    t = random.randint(1, 49);
    y = random.randint(1, 49);
    num1.set(q)
    num2.set(w)
    num3.set(e)
    num4.set(r)
    num5.set(t)
    num6.set(y)
    return

Lottery = Tk()
Lottery.geometry('800x600')
frame = Frame(Lottery)
frame.pack()
Lottery.title('Lotto number generator')

num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()

var = StringVar()
var.set("Lotto Numbers")
frame1 = Frame(Lottery)
frame.pack(side = TOP)
Label = Label(frame1, textvariable=var, font = ("Arial", 48), width=24)
Label.pack(side = TOP)
Label = Label(frame1, textvariable="", width=24)
Label.pack(side = TOP)
Label = Label(frame1, textvariable="", width=24)
Label.pack(side = TOP)

frame2 = Frame(Lottery)
frame2.pack(side = TOP)
txtDisplay= Entry(frame2, textvariable = num1, bd=20, insertwidth=1, font=("Arial", 30))
txtDisplay.pack(side=LEFT)

Lottery.mainloop()
