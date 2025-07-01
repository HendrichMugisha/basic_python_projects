class ATM:
    def __init__(self, balance):
        self.balance=balance
    def check_balance(self):
        print(f"Account Balance={self.balance}")
        
    def deposit(self):
        try:
            self.balance+=float(input("Enter amount to deposit: "))
            print("Deposit successful")
            self.check_balance()
        except ValueError:
            print("Enter valid amount!")

    def withdraw(self):
        try:
            self.balance-=float(input("Enter amount to withdraw: "))
            print("withdraw successful")
            self.check_balance()
        except ValueError:
            print("Enter valid amount!")

    def atm_logic(self):
        while True:
            option=int(input("\nWelcome to the ATM!\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit\nPlease choose an option: "))
            if option==1:
                self.check_balance()
            elif option==2:
                self.deposit()
            elif option==3:
                self.withdraw()
            elif option==4:
                break
user1=ATM(500)
user1.atm_logic()             