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

root.mainloop()
