from tkinter import *
from playsound import playsound

root = Tk()
root.title("Good luck players!")

# SETTING THE SIZE
root.geometry("800x900")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='grey')

user_numbers = LabelFrame(root, text="Enter Your Numbers :", width=700, height=200, fg="salmon", font=("Consolas 20 bold underline"))
user_numbers.place(x=25, y=40)
box1 = Spinbox(user_numbers, from_=0, to=49, width=2, font=("Consolas 35 bold"))
box1.place(x=55, y=50)
box2 = Spinbox(user_numbers, from_=0, to=49, width=2, font=("Consolas 35 bold"))
box2.place(x=155, y=50)
box3 = Spinbox(user_numbers, from_=0, to=49, width=2, font=("Consolas 35 bold"))
box3.place(x=255, y=50)
box4 = Spinbox(user_numbers, from_=0, to=49, width=2, font=("Consolas 35 bold"))
box4.place(x=355, y=50)
box5 = Spinbox(user_numbers, from_=0, to=49, width=2, font=("Consolas 35 bold"))
box5.place(x=455, y=50)
box6 = Spinbox(user_numbers, from_=0, to=49, width=2, font=("Consolas 35 bold"))
box6.place(x=555, y=50)
claimBtn = Button(root, text="Play ball!", borderwidth="3", bg="salmon", width="10", font=("Consolas 20 bold"))
claimBtn.place(x=250, y=255)


# ENTRY BOXES FOR THE RANDOM SELECTION OF NUMBERS
winning_numbers = Label(root, text="The Winning Numbers Are :", fg="salmon", font=("Consolas 20 bold underline"))
winning_numbers.place(x=50, y=350)
WinBox1 = Entry(root, width=2, font=("Consolas 40 bold"))
WinBox1.place(x=50, y=450)
WinBox2 = Entry(root, width=2, font=("Consolas 40 bold"))
WinBox2.place(x=150, y=450)
WinBox3 = Entry(root, width=2, font=("Consolas 40 bold"))
WinBox3.place(x=250, y=450)
WinBox4 = Entry(root, width=2, font=("Consolas 40 bold"))
WinBox4.place(x=350, y=450)
WinBox5 = Entry(root, width=2, font=("Consolas 40 bold"))
WinBox5.place(x=450, y=450)
WinBox6 = Entry(root, width=2, font=("Consolas 40 bold"))
WinBox6.place(x=550, y=450)

border1 = Label(root, text="********************************************************************************************************************", bg="white")
border2 = Label(root, text="********************************************************************************************************************", bg="white")
border1.place(y=560)
border2.place(y=750)
claimBtn = Button(root, text="Claim Your Prize", borderwidth="3", bg="salmon", font=("Consolas 20 bold"))
claimBtn.place(x=20, y=800)
root.mainloop()

