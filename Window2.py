from tkinter import *
from tkinter import messagebox
from datetime import date, datetime, timedelta
from validate_email import validate_email
from playsound import playsound
import rsaidnumber
from dateutil.relativedelta import relativedelta


class InvalidEmail(Exception):
    pass


root = Tk()
root.title("Credential Check")
# SETTING THE SIZE
root.geometry("550x500")

# THE USER CAN'T MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='grey')

now = datetime.now()
# NAME AND SURNAME
nameLBL = Label(root, text="Name and Surname :", bg='grey', font=("Consolas 15 bold"))
nameLBL.place(x=5, y=20)
nameEnt = Entry(root)
nameEnt.place(x=250, y=20)

# ID NUMBER
idLBL = Label(root, text="Enter ID number :", bg="grey", font=("Consolas 15 bold"))
idLBL.place(x=5, y=100)
idEnt = Entry(root)
idEnt.place(x=250, y=100)


def id_check():
    my_id = rsaidnumber.parse(idEnt.get())
    dob = my_id.date_of_birth
    age = relativedelta(date.today(), dob.date())
    return age.years


# EMAIL ADDRESS
emailLBL = Label(root, text="Email Address :", bg='grey', font=("Consolas 15 bold"))
emailLBL.place(x=5, y=200)
emailEnt = Entry(root)
emailEnt.place(x=250, y=200)

# YOUR AGE
# ageLBL = Label(root, text="Enter Your Age :", bg='grey', font=("Consolas 15 bold"))
# ageLBL.place(x=5, y=300)
# ageEnt = Entry(root)
# ageEnt.place(x=250, y=300)


def check():
    try:
        print(type(id_check()))
        rsaidnumber.parse(idEnt.get())

        if not validate_email(emailEnt.get()):
            raise InvalidEmail

        elif id_check() < 18:
            messagebox.showerror(message="Try again when you 18 or older")

        elif id_check() >= 18:
            messagebox.showinfo(message="Lets try and win the big one!")
            w = open("login.txt", "a+")
            w.write("Name : " + nameEnt.get() + "\n" + "Email : " + emailEnt.get() + "\n" + "ID : " + idEnt.get() + "\n" + "Logged Into Game "
                                                                                                 "At :" + str(now) +
                    "\n")
            w.close()
            playsound("sound1.mp3")
            root.destroy()
            import Window3
    except ValueError:
        messagebox.showerror(message="Enter Valid RSA ID")
    except InvalidEmail:
        messagebox.showerror(message="Please enter valid email")


# BUTTON
playBTN = Button(root, text="Lets Play!", command=check, bg="salmon", borderwidth="3", width=20)
playBTN.place(x=50, y=400)


def terminate():
    msg = messagebox.askquestion(message="Would you like to exit?")
    if msg == "yes":
        root.destroy()
    elif msg == "no":
        messagebox.showinfo(message="Returning to the screen")


exitBTN = Button(root, text="Exit", command=terminate, bg="salmon", borderwidth="3", width=20)
exitBTN.place(x=350, y=400)

root.mainloop()

