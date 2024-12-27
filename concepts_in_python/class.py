class Atm:
    #constructor
    
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.menu()
        
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        self.__pin = new_pin
        print("pin changed")
        

    
    def menu(self):
        user_input = input("""
                           Hello, how would you like to proceed?
                           1. Enter 1 to create a new pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
                        """)
        if user_input =="1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()    
        elif user_input == "3":
            self.withdraw()
        elif user_input =="4":
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.__pin = input("enter your pin")
        print("pin created successfully")
        
    def deposit(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            amount = int(input("enter your amount"))
            self.__balance = self.__balance + amount
            print("deposit successful")
        else:
            print("invalid pin")
            
    def withdraw(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            amount = int(input("enter your amount"))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("withdrawl successful")
            else:
                print("not sufficient balance")
        else:
            print("invalid pin")
    
    def check_balance(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")
            
sbi = Atm()

sbi.get_pin()
