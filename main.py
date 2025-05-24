import tkinter, locale
import tkinter.scrolledtext as st
locale.setlocale(locale.LC_ALL,'')

def check(text):
    print(text)

class loan:
    def __init__(self, amount, downpayment, rate, term):
        self.principle = amount
        self.amount = (self.principle-(self.principle*(downpayment/100)))
        self.rate = (rate/100)
        self.term = term

    def monthly_payment(self):
        mpr = self.rate/12
        self.monthly = (self.amount*mpr*(1+mpr)**self.term)/(((1+mpr)**self.term)-1)
        return self.monthly


    def total_interest(self):
        total_interest = round(self.term*self.monthly-self.amount,2)
        total_interest = locale.currency(total_interest, grouping=True)
        return total_interest

    def total_cost(self):
        interest = round(self.term*self.monthly-self.principle,2)
        cost = self.principle + interest
        cost = locale.currency(cost, grouping=True)
        return cost

    def ammoritizer(self):
        month = 1
        mpr = self.rate/12
        payment = self.monthly_payment()
        amount = self.amount
        self.table = []
        while month <= self.term:
            paid_to_interest = (amount*mpr)
            paid_to_principle = (payment-paid_to_interest)
            amount = (amount-paid_to_principle)
            paid_to_principle = locale.currency(paid_to_principle, grouping=True)
            paid_to_interest = locale.currency(paid_to_interest, grouping=True)
            balance = locale.currency(amount,grouping=True)
            line = "Month: {a} Towards Interest: {b} Towards Principle: {c} New Balance: {d}".format(a=month, b=paid_to_interest,c=paid_to_principle,d=balance)
            self.table.append(line)
            month +=1




class app():
    def __init__(self):
        self.w = tkinter.Tk()
        self.w.geometry("900x650+0+0")
        self.w.title("Loan Amortization")
        self.w.config(bg="Light Steel Blue")
        self.framework()
        self.label()
        self.entries()
        self.buttons()
        self.w.mainloop()

    #
    def framework(self):
        self.framed = tkinter.Frame(self.w, bg="Light Steel Blue")
        self.framed.pack(side="top")


    def label(self):
        self.intro = tkinter.Label(self.framed, text = "Loan Ammortirization, please enter loan information bellow.", bg="Light Steel Blue")
        self.intro.grid(column = 0, columnspan = 2, row = 0)
        self.balanceL = tkinter.Label(self.framed, text = "Prinicple: ", pady = 5,bg="Light Steel Blue")
        self.balanceL.grid(column =0, row= 1)
        self.downPaymentL = tkinter.Label(self.framed, text="Down Payment (%): ", pady=5,bg="Light Steel Blue")
        self.downPaymentL.grid(column=0, row=2)
        self.rateL = tkinter.Label(self.framed, text="Rate (APY%): ", pady=5,bg="Light Steel Blue")
        self.rateL.grid(column=0, row=3)
        self.termL = tkinter.Label(self.framed, text="Term (Months): ", pady=5, bg="Light Steel Blue")
        self.termL.grid(column=0, row=4)

    def entries(self):
        self.balance = tkinter.Entry(self.framed,relief = 'sunken')
        self.balance.grid(column = 1,row = 1)
        self.downPayment = tkinter.Entry(self.framed, relief='sunken')
        self.downPayment.grid(column=1, row=2)
        self.rate = tkinter.Entry(self.framed, relief='sunken')
        self.rate.grid(column=1, row=3)
        self.term = tkinter.Entry(self.framed, relief='sunken')
        self.term.grid(column=1, row=4)

    def create_loan(self):
        amount = int(self.balance.get())
        rate = float(self.rate.get())
        term = int(self.term.get())
        downpayment = float(self.downPayment.get())
        self.debt = loan(amount, downpayment, rate, term, )
        self.debt.ammoritizer()
        self.display()

    def buttons(self):
        self.execute = tkinter.Button(self.framed, text = "Do it!", command=lambda:self.create_loan(), bg = "snow")
        self.execute.grid(column = 1, columnspan = 2, row =5)

    def display(self):
        text_area = st.ScrolledText(self.framed,width = 95, wrap = tkinter.WORD)
        text_area.grid(row = 6, columnspan = 2)
        payment = "Your monthly payment would be: " + locale.currency(self.debt.monthly_payment(), grouping=True) +"\n"
        text_area.insert(tkinter.INSERT, payment)
        for i in self.debt.table:
            text_area.insert(tkinter.INSERT, i)
            text_area.insert(tkinter.INSERT, "\n")
        interest = 'Total interest paid: '+ self.debt.total_interest() + " Total Cost: " + self.debt.total_cost()
        text_area.insert(tkinter.INSERT, interest)
        text_area.configure(state='disabled')







root = app()

