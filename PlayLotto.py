# Nathan John Giose- Group2


from tkinter import *
from tkinter import messagebox
import random
from playsound import playsound


# CONFIGURING GUI


root = Tk()
root.config(bg="#069edb")
root.title("Play lotto")
root.geometry("500x650")
#root.resizable(0, 0)

# PICTURE HEADER


img = PhotoImage(file="powerball.png")
canvas = Canvas(root, width=391, height=129)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=55, y=0)

# DEFINING CLASS
# CREATING BUTTONS
# USING OOP FOR ASSIGNMENT PURPOSES- # OOP IS NOT NECESSARY


class allNumbers:
    def __init__(self, lotto):
        # FIRST LINE
        # WE CAN UTILIZE LISTS, BUT FOR ASSIGNMENT PURPOSES, WE MUST DISPLAY 1-49


        self.number_lbl = Label(lotto, text="Lotto Board", font="Arial 12", bg="#069edb")
        self.number_lbl.place(x=120, y=150)
        self.btn1 = Button(lotto, text=1, width=2, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(1))
        self.btn1.place(x=50, y=190)
        self.btn2 = Button(lotto, text=2, width=2, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white",command=lambda: self.on_click(2))
        self.btn2.place(x=100, y=190)
        self.btn3 = Button(lotto, text=3, width=2, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white",command=lambda: self.on_click(3))
        self.btn3.place(x=150, y=190)
        self.btn4 = Button(lotto, text=4, width=2, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white",command=lambda: self.on_click(4))
        self.btn4.place(x=200, y=190)
        self.btn5 = Button(lotto, text=5, width=2, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white",command=lambda: self.on_click(5))
        self.btn5.place(x=250, y=190)
        self.btn6 = Button(lotto, text=6, width=2, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white",command=lambda: self.on_click(6))
        self.btn6.place(x=300, y=190)
        self.btn7 = Button(lotto, text=7, width=2, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white",command=lambda: self.on_click(7))
        self.btn7.place(x=350, y=190)
        self.btn8 = Button(lotto, text=8, width=2, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white",command=lambda: self.on_click(8))
        self.btn8.place(x=400, y=190)

        # NEXT LINE


        self.btn9 = Button(lotto, text=9, width=2, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white", command=lambda: self.on_click(9))
        self.btn9.place(x=50, y=230)
        self.btn10 = Button(lotto, text=10, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(10))
        self.btn10.place(x=100, y=230)
        self.btn11 = Button(lotto, text=11, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(11))
        self.btn11.place(x=150, y=230)
        self.btn12 = Button(lotto, text=12, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(12))
        self.btn12.place(x=200, y=230)
        self.btn13 = Button(lotto, text=13, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(13))
        self.btn13.place(x=250, y=230)
        self.btn14 = Button(lotto, text=14, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(14))
        self.btn14.place(x=300, y=230)
        self.btn15 = Button(lotto, text=15, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(15))
        self.btn15.place(x=350, y=230)
        self.btn16 = Button(lotto, text=16, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(16))
        self.btn16.place(x=400, y=230)

        # NEXT LINE


        self.btn17 = Button(lotto, text=17, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(17))
        self.btn17.place(x=50, y=270)
        self.btn18 = Button(lotto, text=18, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(18))
        self.btn18.place(x=100, y=270)
        self.btn19 = Button(lotto, text=19, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(19))
        self.btn19.place(x=150, y=270)
        self.btn20 = Button(lotto, text=20, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(20))
        self.btn20.place(x=200, y=270)
        self.btn21 = Button(lotto, text=21, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(21))
        self.btn21.place(x=250, y=270)
        self.btn22 = Button(lotto, text=22, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(22))
        self.btn22.place(x=300, y=270)
        self.btn23 = Button(lotto, text=23, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(23))
        self.btn23.place(x=350, y=270)
        self.btn24 = Button(lotto, text=24, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(24))
        self.btn24.place(x=400, y=270)

        # NEXT LINE


        self.btn25 = Button(lotto, text=25, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(25))
        self.btn25.place(x=50, y=310)
        self.btn26 = Button(lotto, text=26, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(26))
        self.btn26.place(x=100, y=310)
        self.btn27 = Button(lotto, text=27, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(27))
        self.btn27.place(x=150, y=310)
        self.btn28 = Button(lotto, text=28, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(28))
        self.btn28.place(x=200, y=310)
        self.btn29 = Button(lotto, text=29, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(29))
        self.btn29.place(x=250, y=310)
        self.btn30 = Button(lotto, text=30, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(30))
        self.btn30.place(x=300, y=310)
        self.btn31 = Button(lotto, text=31, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(31))
        self.btn31.place(x=350, y=310)
        self.btn32 = Button(lotto, text=32, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(32))
        self.btn32.place(x=400, y=310)

        # NEXT LINE


        self.btn33 = Button(lotto, text=33, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(33))
        self.btn33.place(x=50, y=350)
        self.btn34 = Button(lotto, text=34, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(34))
        self.btn34.place(x=100, y=350)
        self.btn35 = Button(lotto, text=35, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(35))
        self.btn35.place(x=150, y=350)
        self.btn36 = Button(lotto, text=36, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(36))
        self.btn36.place(x=200, y=350)
        self.btn37 = Button(lotto, text=37, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(37))
        self.btn37.place(x=250, y=350)
        self.btn38 = Button(lotto, text=38, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(38))
        self.btn38.place(x=300, y=350)
        self.btn39 = Button(lotto, text=39, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(39))
        self.btn39.place(x=350, y=350)
        self.btn40 = Button(lotto, text=40, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(40))
        self.btn40.place(x=400, y=350)

        # NEXT LINE


        self.btn41 = Button(lotto, text=41, bd="0", fg= "green", bg="yellow", activebackground="red", activeforeground="white", command=lambda: self.on_click(41))
        self.btn41.place(x=50, y=390)
        self.btn42 = Button(lotto, text=42, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white", command=lambda: self.on_click(42))
        self.btn42.place(x=100, y=390)
        self.btn43 = Button(lotto, text=43, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white", command=lambda: self.on_click(43))
        self.btn43.place(x=150, y=390)
        self.btn44 = Button(lotto, text=44, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white", command=lambda: self.on_click(44))
        self.btn44.place(x=200, y=390)
        self.btn45 = Button(lotto, text=45, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white", command=lambda: self.on_click(45))
        self.btn45.place(x=250, y=390)
        self.btn46 = Button(lotto, text=46, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white", command=lambda: self.on_click(46))
        self.btn46.place(x=300, y=390)
        self.btn47 = Button(lotto, text=47, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white",command=lambda: self.on_click(47))
        self.btn47.place(x=350, y=390)
        self.btn48 = Button(lotto, text=48, bd="0", fg= "green",bg="yellow", activebackground="red", activeforeground="white", command=lambda: self.on_click(48))
        self.btn48.place(x=400, y=390)

        # NEXT LINE


        self.btn49 = Button(lotto, text=49, bd="0", fg= "yellow",bg="green", activebackground="red", activeforeground="white", command=lambda: self.on_click(49))
        self.btn49.place(x=50, y=430)

        # NEXT LINE
        # DISPLAYS FOR NUMBERS SELECTED


        self.boardA = Label(lotto, width=25, height=2, bg="#069edb", cursor="dot")
        self.boardA.place(x=240, y=450)
        self.boardB = Label(lotto, width=25, height=2, bg="#069edb", cursor="dot")
        self.boardB.place(x=240, y=500)
        self.boardC = Label(lotto, width=25, height=2, bg="#069edb", cursor="dot")
        self.boardC.place(x=240, y=550)

        # BUTTONS


        self.play_btn = Button(lotto, text="Play", bg="#2962ff", bd="0", command=self.play)
        self.play_btn.place(x=175, y=600)
        self.claim_btn = Button(lotto, bg="#2962ff",bd="0", text="Claim Prize", command=self.claim_prize)
        self.claim_btn.place(x=240, y=600)
        self.replay_btn = Button(lotto, text="Play Again", bg="#2962ff", bd="0", command=self.replay)
        self.replay_btn.place(x=350, y=600)
        self.prizes_label = Label(lotto, bg="#069edb")
        self.prizes_label.place(x=50, y=500)
        self.lotto_no = Label(lotto, bg="#2962ff", width=15)
        self.lotto_no.place(x=50, y=550)
        self.root_set1 = []
        self.root_set2 = []
        self.root_set3 = []

    def on_click(self, pick):
        if len(self.root_set1) <= 5 and pick not in self.root_set1:
            self.root_set1.append(pick)
            self.boardA.config(text=self.root_set1)

        elif len(self.root_set1) == 6 and len(self.root_set2) <= 5 and pick not in self.root_set2:
            self.root_set2.append(pick)
            self.boardB.config(text=self.root_set2)

        elif len(self.root_set2) == 6 and len(self.root_set3) <= 5 and pick not in self.root_set3:
            self.root_set3.append(pick)
            self.boardC.config(text=self.root_set3)
        else:
            messagebox.showerror("Error", "Only choose one number")

    def play(self):
        correct = 0
        correct2 = 0
        correct3 = 0
        earnings1 = 0
        earnings2 = 0
        earnings3 = 0
        prizes = [0, 0, 20, 100.50, 2384, 8584, 10000000]
        lotto_list = random.sample(range(1, 49), 6)
        lotto_list.sort()
        matching1 = set(self.root_set1).intersection(set(lotto_list))
        matching2 = set(self.root_set2).intersection(set(lotto_list))
        matching3 = set(self.root_set3).intersection(set(lotto_list))
        for number in self.root_set1:
            if number in lotto_list:
                correct += 1
            if correct == 2:
                earnings1 = prizes[2]
            elif correct == 3:
                earnings1 = prizes[3]
            elif correct == 4:
                earnings1 = prizes[4]
            elif correct == 5:
                earnings1 = prizes[5]
            elif correct == 6:
                earnings1 = prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set one: " + str(correct) + "\nEarnings: " + "R" + str(earnings1) +
                                 "\nMatching number: " + str(matching1))

        for number in self.root_set2:
            if number in lotto_list:
                correct2 += 1
            if correct2 == 2:
                earnings2 = prizes[2]
            elif correct2 == 3:
                earnings2 = prizes[3]
            elif correct2 == 4:
                earnings2 = prizes[4]
            elif correct2 == 5:
                earnings2 = prizes[5]
            elif correct2 == 6:
                earnings2 = prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set one: " + str(correct2) + "\nEarnings: " +
                                 "R" + str(earnings2) + "\nMatching number: " + str(matching2))

        for number in self.root_set3:
            if number in lotto_list:
                correct3 += 1
            if correct3 == 2:
                earnings3 = prizes[2]
                with open("player_id.txt", 'a') as text:
                    text.write('P')
            elif correct3 == 3:
                earnings3 = prizes[3]
            elif correct3 == 4:
                earnings3 = prizes[4]
            elif correct3 == 5:
                earnings3 = prizes[5]
            elif correct3 == 6:
                earnings3 = prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set one: " + str(correct3) + "\nEarnings: " +
                                 "R" + str(earnings3) + "\nMatching number: " + str(matching3))

        if len(self.root_set1) == 6 and len(self.root_set2) == 6 and len(self.root_set3) == 6:
            user_prize = float(earnings1 + earnings2 + earnings3)
            self.prizes_label.config(text="R" + str(user_prize))
            self.lotto_no.config(text=lotto_list)
        else:
            messagebox.showinfo("Error", "Please use all your tries first")


    def claim_prize(self):
        root.destroy()
        import Drag

    def replay(self):
        self.boardA.config(text="")
        self.boardB.config(text="")
        self.boardC.config(text="")
        self.prizes_label.config(text="")
        self.lotto_no.config(text="")
        self.root_set1 = []
        self.root_set2 = []
        self.root_set3 = []


numbers = allNumbers(root)
root.mainloop()
