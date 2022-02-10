class Atm():
    def __init__(self,card_number,pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    
    def cashWithdrawal(self,amount):
        self.amount = amount
        print("You withdrawed " + self.amount)

    def balanceEnquiry(self):
        print("Your current balance is : 10000")

card_num = input("Enter your card number : ")
pin_num = input("Enter the pin of your card : ")
withdraw = input("How much cash you want to withdraw : ")

atmObject = Atm(card_num,pin_num)
atmObject.cashWithdrawal(withdraw)
atmObject.balanceEnquiry()


