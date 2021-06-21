# Nathan John Giose- Group2

from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("LOTTERY GAME")
root.config(bg='#069edb')
root.resizable(0, 0)

# INSERT IMAGE


img = PhotoImage(file="../powerball.png")
canvas = Canvas(root, width=391, height=129)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=55, y=0)

# Label Frame Board A
spin_boardA = LabelFrame(root, text="Board A", bg='#069edb', bd=4, width=391)
spin_boardA.place(x=55, y=150)



current_value = StringVar(value=0)
current_value.set("Lotto Numbers")



# Spinbox
spin_box = Spinbox(spin_boardA, from_=1, to=49, textvariable=current_value, wrap=True, width=4)
spin_box.pack(side=LEFT)
spin_box1 = Spinbox(spin_boardA, from_=1, to=49, textvariable='', wrap=True, width=4)
spin_box1.pack(side=LEFT)
spin_box2 = Spinbox(spin_boardA, from_=1, to=49, textvariable='', wrap=True, width=4)
spin_box2.pack(side=LEFT)
spin_box3 = Spinbox(spin_boardA, from_=1, to=49, textvariable='', wrap=True, width=4)
spin_box3.pack(side=LEFT)
spin_box4 = Spinbox(spin_boardA, from_=1, to=49, textvariable='', wrap=True, width=4)
spin_box4.pack(side=LEFT)
spin_box5 = Spinbox(spin_boardA, from_=1, to=49, textvariable='', wrap=True, width=4)
spin_box5.pack(side=LEFT)
spin_box6 = Spinbox(spin_boardA, from_=1, to=49, textvariable='', wrap=True, width=4, bg='Aqua')
spin_box6.pack(side=LEFT)
btn_spin = Button(spin_boardA, text="Spin", bg='red', width=8)
btn_spin.pack(side=BOTTOM)


spin_boardB = LabelFrame(root, text="Board B", bd=4, bg='#069edb')
spin_boardB.place(x=55, y=220)
current_value = StringVar(value=0)
spin_box0 = Spinbox(spin_boardB, from_=1, to=49, textvariable=current_value, wrap=True, width=4)
spin_box0.pack(side=LEFT)
spin_box01 = Spinbox(spin_boardB, from_=1, to=49, textvariable='', wrap=True, width=4)
spin_box01.pack(side=LEFT)
spin_box02 = Spinbox(spin_boardB, from_=1, to=49, textvariable='', wrap=True, width=4)
spin_box02.pack(side=LEFT)
spin_box03 = Spinbox(spin_boardB, from_=1, to=49, textvariable='', wrap=True, width=4)
spin_box03.pack(side=LEFT)
spin_box04 = Spinbox(spin_boardB, from_=1, to=49, textvariable='', wrap=True, width=4)
spin_box04.pack(side=LEFT)
spin_box05 = Spinbox(spin_boardB, from_=1, to=49, textvariable='', wrap=True, width=4)
spin_box05.pack(side=LEFT)
spin_box06 = Spinbox(spin_boardB, from_=1, to=49, textvariable='', wrap=True, width=4, bg='Aqua')
spin_box06.pack(side=LEFT)
btn_spin = Button(spin_boardB, text="Spin", bg='red', width=8)
btn_spin.pack(side=BOTTOM)











spin_box.pack()
root.mainloop()
