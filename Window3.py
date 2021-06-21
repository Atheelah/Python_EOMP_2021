from tkinter import *
from tkinter import messagebox
from playsound import playsound

root = Tk()
root.title("Good luck players!")

# SETTING THE SIZE
root.geometry("800x900")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='grey')

user_numbers = LabelFrame(root, text="Enter Your Numbers :", width=700, height=200,
                          font=("Consolas 20 bold underline"))
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


def random_numbers():
    import random
    num_list = []
    while len(num_list) < 6:
        num = random.randint(1, 49)
        num_list.append(num)

    print(num_list)
    WinBox1.config(state="normal")
    WinBox1.delete(0, END)
    WinBox1.insert(0, num_list[0])
    WinBox1.config(state='readonly')

    WinBox2.config(state="normal")
    WinBox2.delete(0, END)
    WinBox2.insert(0, num_list[1])
    WinBox2.config(state="readonly")

    WinBox3.config(state="normal")
    WinBox3.delete(0, END)
    WinBox3.insert(0, num_list[2])
    WinBox3.config(state="readonly")

    WinBox4.config(state="normal")
    WinBox4.delete(0, END)
    WinBox4.insert(0, num_list[3])
    WinBox4.config(state="readonly")

    WinBox5.config(state="normal")
    WinBox5.delete(0, END)
    WinBox5.insert(0, num_list[4])
    WinBox5.config(state="readonly")

    WinBox6.config(state="normal")
    WinBox6.delete(0, END)
    WinBox6.insert(0, num_list[5])
    WinBox6.config(state="readonly")


playBtn = Button(root, text="Play ball!", borderwidth="3", bg="salmon", width="10", font=("Consolas 12 bold"),
                 command=random_numbers)
playBtn.place(x=25, y=255)


def clear():
    box1.config(state='normal')
    box1.delete(0, END)
    box1.insert(END, 0)

    box2.config(state='normal')
    box2.delete(0, END)
    box2.insert(END, 0)

    box3.config(state='normal')
    box3.delete(0, END)
    box3.insert(END, 0)

    box4.config(state='normal')
    box4.delete(0, END)
    box4.insert(END, 0)

    box5.config(state='normal')
    box5.delete(0, END)
    box5.insert(END, 0)

    box6.config(state='normal')
    box6.delete(0, END)
    box6.insert(END, 0)

    WinBox1.config(state='normal')
    WinBox1.delete(0, END)
    WinBox1.config(state='readonly')

    WinBox2.config(state='normal')
    WinBox2.delete(0, END)
    WinBox2.config(state='readonly')

    WinBox3.config(state='normal')
    WinBox3.delete(0, END)
    WinBox3.config(state='readonly')

    WinBox4.config(state='normal')
    WinBox4.delete(0, END)
    WinBox4.config(state='readonly')

    WinBox5.config(state='normal')
    WinBox5.delete(0, END)
    WinBox5.config(state='readonly')

    WinBox6.config(state='normal')
    WinBox6.delete(0, END)
    WinBox6.config(state='readonly')


playBtn = Button(root, text="Clear Entries", borderwidth="3", bg="salmon", width="12", font=("Consolas 12 bold"),
                 command=clear)
playBtn.place(x=570, y=255)

# ENTRY BOXES FOR THE RANDOM SELECTION OF NUMBERS
winning_numbers = Label(root, text="The Winning Numbers Are :", font=("Consolas 20 bold underline"))
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
border1 = Label(root,
                text="********************************************************************************************************************",
                bg="white")
border2 = Label(root,
                text="********************************************************************************************************************",
                bg="white")
border1.place(y=560)
border2.place(y=750)


def prizes():
    list1 = (box1.get(), box2.get(), box3.get(), box4.get(), box5.get(), box6.get())
    list2 = (WinBox1.get(), WinBox2.get(), WinBox3.get(), WinBox4.get(), WinBox5.get(), WinBox6.get())
    result = set(list1).intersection(set(list2))
    print(len(result))
    prize = {6: "R10, 000 000.00", 5: "R8,584.00", 4: "R2,384,00", 3: "R100.50", 2: "R20.00", 1: "R0", 0: "R0"}
    my_key = len(result)
    x = prize.get(my_key)
    reserve.config(text='Your Prize is: {}'.format(x))
    with open("login.txt", "a") as file:
        file.write("Winnings: {} \n".format(x))
    if x != "R0":
        playsound("Sound effect - Win (mp3cut.net).mp3")

    elif x == "R0":
        playsound("Fail Sound Effect (mp3cut.net).mp3")


reserve = Label(root, text="", font=("Consolas 20 bold"))
reserve.place(x=50, y=600)

claimBtn = Button(root, text="Check Your Winnings", borderwidth="3", bg="salmon", font=("Consolas 12 bold"),
                  command=prizes)
claimBtn.place(x=20, y=800)


def nextscreen():
    root.destroy()
    import Window4


claimBtn = Button(root, text="Claim Your Prize", borderwidth="3", bg="salmon", font=("Consolas 12 bold"),
                  command=nextscreen)
claimBtn.place(x=500, y=800)
root.mainloop()
