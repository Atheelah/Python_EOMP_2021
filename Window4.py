from tkinter import *
root = Tk()
root.title("Lottery Machine")
from datetime import date, datetime, timedelta

# SETTING THE SIZE
root.geometry("600x600")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='grey')

# Using OOP to create labels and entries
class Bank:
    def __init__(self, master):
        self.master = master
        self.banking = LabelFrame(self.master, text="Banking Details", width=550, height=500, fg="salmon", font=("Consolas 20 bold underline"))
        self.banking.place(x=25, y=40)
        self.bankLBL = Label(self.banking, text="Bank :", font=("Consolas 10 bold"), bg="salmon")
        self.bankLBL.place(x=5, y=60)
        self.default_bank = "Select Bank"
        self.default_var = StringVar(value=self.default_bank)
        self.bankEnt = OptionMenu(self.banking, self.default_var, "ABSA Bank", "Capitec Bank", 'Standard Bank', 'NedBank')  # BANKING DETAILS OPTION MENU
        self.bankEnt.place(x=200, y=60)
        self.holderLBL = Label(self.banking, text="Account Holder :", font=("Consolas 10 bold") ,bg="salmon")
        self.holderLBL.place(x=5, y=120)
        self.holderEnt = Entry(self.banking)
        self.holderEnt.place(x=200, y=120)
        self.numberLBL = Label(self.banking, text="Account Number :",  font=("Consolas 10 bold") ,bg="salmon")
        self.numberLBL.place(x=5, y=180)
        self.numberEnt = Entry(self.banking)
        self.numberEnt.place(x=200, y=180)
        self.branchLBL = Label(self.banking, text="Branch :", font=("Consolas 10 bold") ,bg="salmon")
        self.branchLBL.place(x=5, y=240)
        self.branchEnt = Entry(self.banking)
        self.branchEnt.place(x=200, y=240)
        self.cvvLBL = Label(self.banking, text="CVV :", font=("Consolas 10 bold") ,bg="salmon")
        self.cvvLBL.place(x=5, y=300)
        self.cvvEnt = Entry(self.banking)
        self.cvvEnt.place(x=200, y=300)
        self.expiryLBL = Label(self.banking, text="Expiry :", font=("Consolas 10 bold"), bg="salmon")
        self.expiryLBL.place(x=5, y=360)
        self.expiryEnt = Entry(self.banking)
        self.expiryEnt.place(x=200, y=360)
        self.clearBTN = Button(self.banking, text="CLear Entries", font=("Consolas 10 bold"), bg="salmon", command=self.clear, borderwidth="3")
        self.clearBTN.place(x=50, y=400)
        self.clearBTN = Button(self.banking, text="Proceed to Next Screen", font=("Consolas 10 bold"), bg="salmon", command=self.proceed, borderwidth="3")
        self.clearBTN.place(x=300, y=400)
        self.prize = Label(self.banking, text="Proceed to next screen to convert your prize to another currency", font=("Consolas 10 bold"))
        self.prize.place(x=10, y=440)


# DEFINING A CLEAR BUTTON USING OOP
    def clear(self):

        self.holderEnt.delete(0, END)
        self.default_var.set("Select Bank")  # ALLOWS THE OPTION MENU TO CLEAR AND TO GO BACK TO DEFAULT
        self.numberEnt.delete(0, END)
        self.branchEnt.delete(0, END)
        self.cvvEnt.delete(0, END)
        self.expiryEnt.delete(0, END)

    def proceed(self):  # CREATING A TXT FILE FOR BANKING, WHERE ALL THE BANKING DETAILS GET STORED
        now = datetime.now()
        w = open("Banking.txt", "a+")
        w.write("Holder: " + self.holderEnt.get() + "\n" + "Account Number: " +
                self.numberEnt.get() + "\n" + "Branch: " + self.branchEnt.get() + "\n" + "CVV: " +
                self.cvvEnt.get() + "\n" + "Expiry: " + self.expiryEnt.get() + "\n" + "Provided Banking Details "
                                                                                            "At :" + str(now) + "\n")
        w.close()
        self.master.destroy()
        import Window5  # IMPORTS THE NEXT WINDOW


Bank(root)
root.mainloop()
