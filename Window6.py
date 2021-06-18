from tkinter import *

root = Tk()
root.title("Lottery Machine")

# SETTING THE SIZE
root.geometry("400x250")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='grey')
thanksLBL = Label(root, text="Thank You For PLaying With")
thanksLBL2 = Label(root, text="Ithuba National Lottery")
thanksLBL3 = Label(root, text="of")
thanksLBL4 = Label(root, text="South Africa.")
thanksLBL5 = Label(root, text="Thank You for being a great sport,")
thanksLBL6 = Label(root, text="We Hope You Are Happy With Your Earnings!")

header = Label(root, text="Thank You For Playing With ", fg='salmon', bg='grey', font=("Consolas 15 bold"))
header.place(x=50, y=20)
header2 = Label(root, text="Ithuba National Lottery ", fg='salmon', bg='grey', font=("Consolas 15 bold"))
header2.place(x=50, y=50)
header3 = Label(root, text="of", fg='salmon', bg='grey', font=("Consolas 15 bold"))
header3.place(x=170, y=80)
header4 = Label(root, text="South Africa", fg='salmon', bg='grey', font=("Consolas 15 bold"))
header4.place(x=115, y=110)
root.mainloop()
