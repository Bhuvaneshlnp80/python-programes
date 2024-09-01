class bank():
    bankname='canara bank'
    
    def __init__(self,name,accno,balance):
        self.name=name
        self.accno=accno
        self.balance=balance
        
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('new balance:',self.balance)
        
    def withdraw(self,amount):
        if amount>self.balance:
            print("insuficient")
        else:
            self.balance=self.balance-amount
            print('new balance: ',self.balance)
        
    
print('welcome to ',bank.bankname)
name=input('user name:')
accno=int(input('account number :'))
balance=int(input('current balance :'))
bank1=bank(name,accno,balance)
amount=int(input('amount is:'))
while 1:
    n=input('user input:')
    if n=='d':
        bank1.deposit(amount)
    elif n=='w':
        bank1.withdraw(amount)
    elif n == 'q':
        print("Thank you for using Canara Bank!")
        break
    else:
        print("Invalid input. Please enter 'd', 'w', or 'q'.")