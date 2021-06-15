from tkinter import *

root = Tk()
root.title("Lottery Machine")

# SETTING THE SIZE
root.geometry("500x500")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='grey')

banking = LabelFrame(root, text="Banking Details", width=450, height=400, fg="salmon", font=("Consolas 20 bold underline"))
banking.place(x=25, y=40)
bankLBL = Label(banking, text="Bank :", font=("Consolas 10 bold"), bg="salmon")
bankLBL.place(x=5, y=60)
default_bank = "Select Bank"
default_var = StringVar(value=default_bank)
bankEnt = OptionMenu(banking, default_var, "rdftgyhu", "fghjk", 'dfghuji', 'dfghji')
bankEnt.place(x=200, y=60)
holderLBL = Label(banking, text="Account Holder :", font=("Consolas 10 bold") ,bg="salmon")
holderLBL.place(x=5, y=120)
holderEnt = Entry(banking)
holderEnt.place(x=200, y=120)

root.mainloop()
