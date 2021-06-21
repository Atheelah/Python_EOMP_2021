from tkinter import *

root = Tk()
root.title("Lottery Machine")

# SETTING THE SIZE
root.geometry("400x300")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='grey')
thanksLBL = Label(root, text="Thank You For PLaying With")
thanksLBL2 = Label(root, text="Ithuba National Lottery")
thanksLBL3 = Label(root, text="of")
thanksLBL4 = Label(root, text="South Africa.")


header = Label(root, text="Thank You For Playing With ", bg='grey', font=("Consolas 15 bold"))
header.place(x=50, y=20)
header2 = Label(root, text="Ithuba National Lottery ", bg='grey', font=("Consolas 15 bold"))
header2.place(x=50, y=50)
header3 = Label(root, text="of", bg='grey', font=("Consolas 15 bold"))
header3.place(x=170, y=80)
header4 = Label(root, text="South Africa", bg='grey', font=("Consolas 15 bold"))
header4.place(x=115, y=110)
thanksLBL5 = Label(root, text="Thank You for being a great sport,", bg='grey', font=("Consolas 15 bold"))
thanksLBL5.place(x=0, y=145)
thanksLBL6 = Label(root, text="We Hope You Are Happy", bg='grey', font=("Consolas 15 bold"))
thanksLBL6.place(x=70, y=175)
thanksLBL7 = Label(root, text="With Your Earnings!", bg="grey", font=("Consolas 15 bold"))
thanksLBL7.place(x=75, y=205)


def exit():
    root.destroy()


button = Button(root, text="Exit", borderwidth="3", bg="salmon", font=("Consolas 10 bold"), command=exit)
button.place(x=330, y=255)
root.mainloop()
