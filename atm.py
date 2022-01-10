class atm(object):
    def __init__(self, card, pin):
        self.card=card
        self.pin=pin
        self.newCash=50000
    def cashWithdrawl(self, amt):
        self.newCash=self.newCash-amt
        print("Cash withdrawled")
        print("your remaining balance is ",self.newCash)
    def checkBalance(self):
        print("you have ", self.newCash, " dollars")
        
def main():
    cardNumber=input("Whats your card number")
    pinNumber=input("whats your pin")

    User=atm(cardNumber, pinNumber)
    print("what are you here for")
    print("1. Cash info 2. withdrawl")
    activity=int(input("enter 1 or 2"))
    if(activity==2):
        amt=int(input("How much ca$h do you want"))
        User.cashWithdrawl(amt)
    elif(activity==1):
        User.checkBalance()
    else:
        print("You either misclicked or you can't read or you want to know what will happen or you are just an idiot")
main()