from abc import ABC , abstractmethod

class Account(ABC):

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withDraw(self):
        pass

class SavingAccount(Account):

    __balance = 0

    def get_balance(self):
        # print("Balance = ",self.__balance)
        return self.__balance

    def deposit(self):
        amount=int(input("Enter  deposited amount: "))
        self.__balance += amount
        print("Amount depoisted : ",self.__balance)

    def withDraw(self):
        amount=int(input("Enter withdrawn amount: "))

        if self.__balance > amount:
            print("Not Enough Balance") 
            return   
            
        self.__balance - self.amount
        print("Amount withdrawn : " , self.__balance)

            


class CurrentAccount(Account):

    __balance = 0
    withDraw_limit = 0

    def __init__(self , limit):
        self.withDraw_limit = limit

    def get_balance(self):
        # print("Balance = ",self.__balance)
        return self.__balance

    def deposit(self,amount):
        amount
        self.amount =int(input("Enter deposited amount:"))
        self.__balance += self.amount
        print("Amount depoisted : ", self.amount)

    def withDraw(self , amount):
        amount=0
        self.amount=int(input("Enter withdraw amount: "))

        if self.__balance + self.withDraw_limit < amount:
            print("Not Enought Balance")
            return

        self.withDraw_limit= amount
        print("Amount withdrawn : " , self.amount)
        

class Bank:

    owner = "bank"
    account_number = 0
    

    def __init__(self , name , number , account_type = " "):
        self.name=input("Enter name: ")
        self.owner = name
        self.number=int(input("Enter number: "))
        self.account_number = number


        if account_type == "Saving":
            self.account = SavingAccount()
        if account_type == "Current":
            self.account = CurrentAccount(5000)


class Manager:

    def get_customer_info(self , bankAccount : Bank):
        self.bankAccount=int(input("Enter bank account: "))
        print(f"Name : {bankAccount.owner}")
        print(f"AccountNumber : {bankAccount.account_number}")
        print("Account Type : ", end="")
        if(type(bankAccount.account) == SavingAccount):
            print("Savings Account")
        elif (type(bankAccount.account) == CurrentAccount):
    
            print("Current Account")
        else:
            print("Account Not Found")
        # print(f"Account Type : {"Savings Account" if type(bankAccount.account) == SavingAccount else "Current Account"}")
        print(f"Balance : {bankAccount.account.get_balance()}")

    def __str__(self):
        return "Manager Object bro"

ram = Bank("Ram" , 1 , "Saving")
ram.account.deposit()
ram.account.withDraw()



print("<===== Sam Account =====>")
sam = Bank("Sam" , 2 , "Current")
sam.account.deposit(48)
sam.account.withDraw(0)

dk = Manager()
while True:
    if Account==CurrentAccount:
        print("<===== Ram Account =====>\t")
        dk.get_customer_info(ram)
    else:
        print("<===== Sam Account =====>\t")
        dk.get_customer_info(sam)
#print(type(dk) == Manager)

