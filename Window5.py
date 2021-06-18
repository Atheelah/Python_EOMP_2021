from tkinter import *
import requests
root = Tk()
root.title("Let's Convert Your Winnings !")


# SETTING THE SIZE
root.geometry("600x600")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='grey')
currency = LabelFrame(root, height=550, width=500, text="Lets Convert Your Winnings", font=("Consolas 15 bold"))
currency.place(x=25, y=25)
currencyLBL = Label(currency, text="Enter Your Currency Code Here :", font=("Consolas 15 bold"), bg="salmon")
currencyLBL.place(x=30, y=10)
currencyEnt = Entry(currency,  font=("Consolas 20 bold"), width=23)
currencyEnt.place(x=30, y=50)
cashLBL = Label(currency, text="Enter Your Winnings Here :", font=("Consolas 15 bold"), bg="salmon" )
cashLBL.place(x=30, y=120)
cashEnt = Entry(currency, font=("Consolas 20 bold"), width=23)
cashEnt.place(x=30, y=160)


def conversion():
    url = "https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR"
    information = requests.get(url).json()
    output = int(cashEnt.get()) * information["conversion_rates"][currencyEnt.get()]
    print(output)
    answerEnt.insert(0, "{} ({})".format(output, currencyEnt.get()))


def clear():
    currencyEnt.delete(0, END)
    cashEnt.delete(0, END)
    answerEnt.delete(0, END)


convertBTN = Button(currency, text="Lets Convert!", font=("Consolas 10 bold"), bg="salmon", borderwidth="5", command=conversion)
convertBTN.place(x=5, y=220)
convertBTN = Button(currency, text="CLear Entries", font=("Consolas 10 bold"), bg="salmon", borderwidth="5", command=clear)
convertBTN.place(x=300, y=220)
border1 = Label(currency, text="************************************************************************************", bg="grey", fg="salmon")
border1.place(y=300)


answerLBL = Label(currency, text="Your New Currency is : ", font=("Consolas 15 bold"), bg="salmon")
answerLBL.place(x=30, y=360)
answerEnt = Entry(currency, font=("Consolas 20 bold"), width=23)
answerEnt.place(x=30, y=400)

border2 = Label(currency, text="************************************************************************************", bg="grey", fg="salmon")
border2.place(y=490)

root.mainloop()

