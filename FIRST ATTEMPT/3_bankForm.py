# Nathan John Giose- Group2

from tkinter import *
import os
import rsaidnumber


# GUI DESIGN


bank_win = Tk()
bank_win.title('Lotto Draw')
bank_win.config(bg="#069edb")
bank_win.geometry("500x250")

# INSERT IMAGE


img = PhotoImage(file="../powerball.png")
canvas = Canvas(bank_win, width=391, height=129)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack()


# FUNCTIONS


def end_reg():
    name = temp_name.get()
    id = temp_id.get()
    email = temp_email.get()
    address = temp_address.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if name == "" or id == "" or address == "" or password == "" or email == "":
        notify.config(fg="red",text="All fields requried * ")
        return

    for name_check in all_accounts:
        if name == name_check:
            notify.config(fg="red",text="Account already exists")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(id+'\n')
            new_file.write(address+'\n')
            new_file.write('0')
            new_file.close()
            notify.config(fg="green", text="Account has been created")

def register():
    #Vars
    global temp_name
    global temp_id
    global temp_address
    global temp_email
    global temp_password
    global notify
    temp_name = StringVar()
    temp_id = StringVar()
    temp_address = StringVar()
    temp_email = StringVar()
    temp_password = StringVar()















    #Register Screen
    info_win = Toplevel(bank_win)
    info_win.title('Register')
    info_win.config(bg="#069edb")
    info_win.geometry("400x400")

    # INSERT IMAGE


    img = PhotoImage(file="../powerball.png")
    canvas = Canvas(info_win, width=391, height=129)
    canvas.create_image(0, 0, anchor=NW, image=img)
    canvas.pack()

    # LABEL FOR INFO
    Label(info_win, bg="#069edb", text="Please enter your details below to register", font=('Arial',12)).place(x=55, y=150)

    # LABEL FOR INPUTS
    Label(info_win, bg="#069edb", text="Name", font=('Arial',12)).place(x=28, y=180)
    Label(info_win, bg="#069edb", text="Email", font=('Arial',12)).place(x=28, y=270)
    Label(info_win, bg="#069edb", text="Address", font=('Arial',12)).place(x=28, y=240)
    Label(info_win, bg="#069edb", text="ID", font=('Arial',12)).place(x=28, y=210)
    Label(info_win, bg="#069edb", text="Password", font=('Arial',12)).place(x=28, y=300)
    notify = Label(info_win, bg="#069edb", font=('Arial',12))
    notify.place(x=28, y=360)

    # ENTRIES FOR INPUT DATA
    Entry(info_win,textvariable=temp_name).place(x=130, y=180)
    Entry(info_win,textvariable=temp_id).place(x=130, y=210)
    Entry(info_win,textvariable=temp_address).place(x=130, y=240)
    Entry(info_win,textvariable=temp_email).place(x=130, y=270)
    Entry(info_win,textvariable=temp_password,show="*").place(x=130, y=300)

    #Buttons
    Button(info_win, text="Register", command = end_reg, font=('Arial',12)).place(x=130, y=330)















def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password  = file_data[1]
            #Account Dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(bank_win)
                account_dashboard.title('Dashboard')
                #Labels
                Label(account_dashboard, text="Account Dashboard", font=('Arial',12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Welcome "+name, font=('Arial',12)).grid(row=1,sticky=N,pady=5)
                #Buttons
                Button(account_dashboard, text="Personal Details",font=('Arial',12),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                return
            else:
                login_notify.config(fg="red", text="Password incorrect!!")
                return
    login_notify.config(fg="red", text="No account found !!")

def personal_details():
    #Vars
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_address = user_details[2]
    details_id = user_details[3]
    details_balance = user_details[4]


    #Personal details screen
    personal_details_screen = Toplevel(bank_win)
    personal_details_screen.title('Personal Details')


    #Labels
    Label(personal_details_screen, text="Personal Details", font=('Arial',12)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen, text="Name : "+details_name, font=('Arial',12)).grid(row=1,sticky=W)
    Label(personal_details_screen, text="ID : "+details_id, font=('Arial',12)).grid(row=2,sticky=W)
    Label(personal_details_screen, text="address : "+details_address, font=('Arial',12)).grid(row=3,sticky=W)
    Label(personal_details_screen, text="Balance :R"+details_balance, font=('Arial',12)).grid(row=4,sticky=W)
def login():
    #Vars
    global temp_login_name
    global temp_login_password
    global login_notify
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    #Login Screen
    login_screen = Toplevel(bank_win)
    login_screen.title('Login')
    #Labels
    Label(login_screen, text="Login to your account", font=('Arial',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Username", font=('Arial',12)).grid(row=1,sticky=W)
    Label(login_screen, text="Password", font=('Arial',12)).grid(row=2,sticky=W)
    login_notify = Label(login_screen, font=('Arial',12))
    login_notify.grid(row=4,sticky=N)
    #Entry
    Entry(login_screen, textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_password,show="*").grid(row=2,column=1,padx=5)
    #Button
    Button(login_screen, text="Login", command=login_session, width=15,font=('Arial',12)).grid(row=3,sticky=W,pady=5,padx=5)


#Labels
# Label(bank_win, text = "the most secure bank you've probably used", font=('Arial',12)).grid(row=1,sticky=N)


#Buttons
Button(bank_win, text="Register", font=('Arial',12),width=20,command=register).place(x=140, y=150)
Button(bank_win, text="Login", font=('Arial',12),width=20,command=login).place(x=140, y=200)

bank_win.mainloop()
