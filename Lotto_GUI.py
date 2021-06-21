# Nathan John Giose- Group 2
# I will import everything from tkinter, as well as the messagebox
# Then from datetime I'll import datetime and timedelta
# I will import rsaidnumber for the id number


from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta
import rsaidnumber
import os
import validate_email

# Designing the interface


window = Tk()
window.config(bg="#069edb")
window.title("LOTTERY GAME")
window.geometry("500x500")
window.resizable(0, 0)

# INSERT IMAGE


img = PhotoImage(file="powerball.png")
canvas = Canvas(window, width=391, height=129)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack()

# Inserting the labels and entry boxes in the Authentication class


class Authentication:

    def __init__(self, root):
        self.name_lbl = Label(root, text="Please enter your name", font=('Arial', 12), bg="#069edb", bd=3)
        self.name_lbl.place(x=53, y=150)
        self.name_entry = Entry(root)
        self.name_entry.place(x=280, y=150)

        self.email_lbl = Label(root, text="Please enter your email", font=('Arial', 12), bg="#069edb", bd=3)
        self.email_lbl.place(x=53, y=200)
        self.email_entry = Entry(root)
        self.email_entry.place(x=280, y=200)

        self.address_lbl = Label(root, text="Please enter your address", font=('Arial', 12), bg="#069edb", bd=3)
        self.address_lbl.place(x=53, y=250)
        self.address_entry = Entry(root)
        self.address_entry.place(x=280, y=250)

        self.identity_lbl = Label(root, text="Please enter your ID number", font=('Arial', 12), bg="#069edb", bd=3)
        self.identity_lbl.place(x=53, y=300)
        self.identity_entry = Entry(root)
        self.identity_entry.place(x=280, y=300)

        self.authentication_btn = Button(root, text="Confirm", command=self.age_check)
        self.authentication_btn.place(x=215, y=350)


        if self.name_entry == "" or self.email_entry == "" or self.email_entry == "" or self.email_entry == "":
            messagebox.showerror("Error","All fields requried * ")





# Age check


    def age_check(self):
        player_ID = open("player_id.txt","a+")
        player_ID.write(self.name_entry.get())
        player_ID.write('\n')
        player_ID.write(self.email_entry.get()+'\n')
        player_ID.write(self.address_entry.get()+'\n')
        player_ID.write(self.identity_entry.get()+'\n')
        player_ID.write('0')
        player_ID.close()
        messagebox.showinfo("Info", "Information being recorded")

        id_number = rsaidnumber.parse(self.identity_entry.get())
        age = str((datetime.today() - id_number.date_of_birth) // timedelta(days=365.25))
        #print(age)
        try:
            if int(age) >= 18:
                messagebox.showinfo("Congratulations!", "You qualify to play")
                window.destroy()
                import PlayLotto
            elif int(age) < 18:
                ages = str(int(age) - 18)
                messagebox.showerror("Error", "You're not of age to Gamble! You can play in" + ages + " year/s")
           #     print(ages)
        except ValueError:
            messagebox.showerror("Error", "Invalid ID number")

# Running the program


authentication = Authentication(window)
window.mainloop()
