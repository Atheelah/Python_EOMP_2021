# INSTALLING  THE MODULES THAT ARE NEEDED
from tkinter import *
from tkinter import messagebox
from datetime import date, datetime, timedelta
from validate_email import validate_email
from playsound import playsound
import rsaidnumber
from dateutil.relativedelta import relativedelta

# CREATING MY OWN EXCEPTION
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

# DEFINING A FUNCTION FOR ID. CHECKS HOW OLD THE PERSON IS BY THE ID NUMBER
def id_check():
    my_id = rsaidnumber.parse(idEnt.get())
    dob = my_id.date_of_birth
    age = relativedelta(date.today(), dob.date())
    return age.years


# EMAIL ADDRESS LABEL
emailLBL = Label(root, text="Email Address :", bg='grey', font=("Consolas 15 bold"))
emailLBL.place(x=5, y=200)
emailEnt = Entry(root)
emailEnt.place(x=250, y=200)

# DEFINING A FUNCTION TO CHECK IF THE PERSON IS OLD ENOUGH TO PLAY
def check():
    try:  # GETTING THE ID
        print(type(id_check()))
        rsaidnumber.parse(idEnt.get())

        if not validate_email(emailEnt.get()):  # VALIDATING THE INPUT OF THE EMAIL
            raise InvalidEmail

        elif id_check() < 18:  # CHECKS IF THE PLAYER IS YOUNGER THAN 18, SHOWS ERROR MESSAGE
            messagebox.showerror(message="Access Denied. Try again when you 18 or older")

        elif id_check() >= 18:  # CHECKS IF THE PLAYER IS 18 OR OLDER, ACCESS INTO THE GAME IS GRANTED
            messagebox.showinfo(message="Access Granted! Lets play")

            w = open("login.txt", "a+")  # THE INFORMATION IS RECORDED AND GETS STORED IN A TXT FILE.
            w.write("Name : " + nameEnt.get() + "\n" + "Email : " + emailEnt.get() + "\n" + "ID : " + idEnt.get() + "\n" + "Logged Into Game "
                                                                                            "At :" + str(now) +
                    "\n")
            w.close()
            playsound("sound1.mp3")  # ONCE ACCESS IS GRANTED A SOUND GETS PLAYED
            root.destroy()
            import Window3  # WINDOW 3 GETS IMPORTED
    except ValueError:
        messagebox.showerror(message="Enter Valid RSA ID")  # HAPPENS WHEN USER INPUTS A WRONG ID
    except InvalidEmail:
        messagebox.showerror(message="Please enter valid email")  # HAPPENS WHEN USER INPUTS A WRONG EMAIL


# BUTTON
playBTN = Button(root, text="Lets Play!", command=check, bg="salmon", borderwidth="3", width=20)
playBTN.place(x=50, y=400)


# DEFINING AN EXIT BUTTON
def terminate():
    msg = messagebox.askquestion(message="Would you like to exit?")
    if msg == "yes":
        root.destroy()
    elif msg == "no":
        messagebox.showinfo(message="Returning to the screen")


exitBTN = Button(root, text="Exit", command=terminate, bg="salmon", borderwidth="3", width=20)
exitBTN.place(x=350, y=400)

root.mainloop()

