from tkinter import *
import tkinter
from tkinter import messagebox
import requests


# initialise the self
window = Tk()
window.title("Banking Details")
window.geometry("900x450")
window.config(bg="#069edb")

# IMAGE


img = PhotoImage(file="powerball.png")
canvas = Canvas(window, width=391, height=129)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack()


class inherit:
    def __init__(self, window):
        self.label = Label(window, text="Enter your banking details", fg="black", bg="#069edb", font=("Arial", 30)).pack()
        self.account_holder_name_entry = Entry(window)
        self.account_holder_name_entry.place(x=400, y=200)
        self.account_holder_name_label = Label(window, text="Account Holder Name", bg="#069edb", font=("Arial", 13))
        self.account_holder_name_label.place(x=170, y=200)
        self.account_number_entry = Entry(window)
        self.account_number_entry.place(x=400, y=240)
        self.account_number_label = Label(window, text="Account Number", bg="#069edb", font=("Arial", 13))
        self.account_number_label.place(x=170, y=240)
        self.variable = StringVar()
        self.variable.set('BANK BRANCH')
        self.bank_opt = OptionMenu(window, self.variable, 'FNB', 'Capitec', 'Netbank', 'Standard Bank')
        self.bank_opt.place(x=630, y=200)
        self.currency_entry = Entry(window)
        self.currency_entry.place(x=400, y=280)
        self.currency_label = Label(window, text="Enter currency code", bg="#069edb", font=("Arial", 13))
        self.currency_label.place(x=170, y=280)
        self.email_entry = Entry(window)
        self.email_entry.place(x=400, y=320)
        self.email_label = Label(window, text="Email", bg="#069edb", font=("Arial", 13))
        self.email_label.place(x=170, y=320)


        def currency_converter():
            response = requests.get("https://v6.exchangerate-api.com/v6/3b6104d9c62069d198e73219/latest/")
            data = response.json()



        def enter():
            try:
                list1 = ["1", "2", "3", "4", '5', "6", "7", "8", '9', "0"]
                name_ent = self.account_holder_name_entry.get()
                number_ent = self.account_number_entry.get()
                with open("player_id.txt", "a+") as info:
                    info.write(self.account_holder_name_entry.get())
                    info.write('\n')
                    info.write(self.account_number_entry.get()+'\n')
                    info.write(self.currency_entry.get()+'\n')
                    info.write(self.email_entry.get()+'\n')
                if name_ent == '':
                    raise ValueError
                elif name_ent in list1:
                    raise ValueError
                if number_ent == '':
                    raise ValueError
                else:
                    int(self.account_number_entry.get())
                    messagebox.showinfo(message='Details have been entered correctly:)')
                if self.variable.get() == 'Select Bank':
                    raise ValueError
                elif self.variable.get() == 'FNB':
                    messagebox.showinfo(message='Details have been entered correctly:)')
                elif self.variable.get() == 'Capitec':
                    messagebox.showinfo(message='Details have been entered correctly:)')
                elif self.variable.get() == 'Netbank':
                    messagebox.showinfo(message='Details have been entered correctly:)')
                elif self.variable.get() == 'Standard Bank':
                    messagebox.showinfo(message='Details have been entered correctly:)')
            except ValueError:
                messagebox.showerror(message='Something went wrong! Please ensure that fields are entered correctly')

        # Buttons
        enter_button = Button(window, text="Enter", command=enter, height=2, width=10, bg="#006466", fg="Black").place(x=280, y=400)
        exit_button = Button(window, text="Exit", command=exit, height=2, width=10, bg="#006466", fg="Black").place(x=490, y=400)


# Running the program
inherit(window)
window.mainloop()
