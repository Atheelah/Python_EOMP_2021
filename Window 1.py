# ATHEELAH VAN DER SCHYFF
# CLASS 1

from tkinter import *

root = Tk()
root.title("Lottery Machine")

# SETTING THE SIZE
root.geometry("400x250")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='grey')

# WELCOME MESSAGE
header = Label(root, text="Welcome To ", fg='salmon', bg='grey', font=("Consolas 15 bold"))
header.place(x=120, y=20)
header2 = Label(root, text="Ithuba National Lottery ", fg='salmon', bg='grey', font=("Consolas 15 bold"))
header2.place(x=50, y=50)
header3 = Label(root, text="of", fg='salmon', bg='grey', font=("Consolas 15 bold"))
header3.place(x=170, y=80)
header4 = Label(root, text="South Africa", fg='salmon', bg='grey', font=("Consolas 15 bold"))
header4.place(x=115, y=110)

# DEFINING A FUNCTION FOR THE NEXT WINDOW
def nextscreen():
    root.destroy()
    import Window2

# CREATING A BUTTON
btn = Button(root, text="Lets Check If You're Old Enough", bg="salmon", borderwidth="3", command=nextscreen)
btn.place(x=70, y=160)

root.mainloop()
