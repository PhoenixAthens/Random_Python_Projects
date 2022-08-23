import random
class Bank:
    def __init__(self,nameOfBank,Address,Rankval):
        self.NameOfBank=nameOfBank
        self.BankAddress=Address
        self.MarketRank=Rankval
    def WithdrawAmount(self):
        raise NotImplementedError
    def DepositAmount(self):
        raise NotImplementedError
    def GetCustomerDetails(self):
        raise NotImplementedError
    def GetCustomerName(self):
        raise NotImplementedError
    def ShowCustomerReport(self):
        raise NotImplementedError
    def UpdateCardNum(self):
        raise NotImplementedError
        
class Account(Bank):
    
    def __init__(self,nameOfBank,Address,Rank,PhNum,NameOfCustomer,Age,Gender,Balance):
        super().__init__(nameOfBank,Address,Rank)
        self.CustomerPhoneNumber=PhNum
        self.NameOfCustomer=NameOfCustomer
        self.AgeOfCustomer=Age
        self.Gender=Gender
        self.Balance=float(Balance)
        self.CardNum=random.randint(1_000_000,10_000_000) 
        self.FileName=f"{self.NameOfCustomer}_{self.CardNum}" 
        #TODO:Creating a file right when we create a customer account automaticallly!
        with open(f"{self.FileName}","a")as file:
            file.write(f"\t\tName of bank: {self.NameOfBank}\n\t\tBank Address: {self.BankAddress}\nName of Customer: {self.NameOfCustomer}\nBalance: {self.Balance}\n")
            file.write(f"Customer PhoneNumber: {self.CustomerPhoneNumber}\nCard Number: {self.CardNum}\n")
        print("Account Successfully Created!")
    
    def WithdrawAmount(self):
        value=float(input("Enter withdraw amount!"))
        if(value<=self.Balance):
            self.Balance-=value
            newBalance=self.Balance
            with open(self.FileName,"a")as file:
                file.write(f"\nAmount Withdrawn: {value}\n Updated Balance: {self.Balance}\n")
            print(f"You have been charged ${value}")
            print(f"You have ${newBalance} amount left in you account!")
        else:
            print("INSUFFICIENT FUNDS")
    
    def DepositAmount(self):
        value=float(input("Enter the amount to be deposited\n"))
        self.Balance+=value
        with open(self.FileName,"a")as file:
            file.write(f"\nAmount Deposited: {value}\nNew Balance: {self.Balance}\n")
        print("Amount Deposited!")
        print(f"You have ${self.Balance} in you account!")
    
    def GetCustomerDetails(self):
        print(f"Customer Name: {self.NameOfCustomer} \nCustomer Age: {self.AgeOfCustomer} \nAccount Balance: {self.Balance} \nCardNumber: {self.CardNum}\nPhoneNumber: {self.CustomerPhoneNumber}")
    
    def ShowCustomerReport(self):
        with open(self.FileName,"r")as file:
            reading=file.readlines()
            for i in reading:
                print(i.rstrip())
    
    def UpdateCardNum(self):
        self.CardNum=random.randint(1_000_000,10_000_000)
    
    def GetCustomerName(self):
        print("Customer Name: "+self.NameOfCustomer)
    
    @property
    def GetCardNumber(self):
        print(self.CardNum)
#TODO:You can put here a while loop to play with actions acting on a account holders account, like use a switch!
#Sample Data for text
c1=Account("SwissBank","NYC,America",9,886024,"Phoenix",19,"M",1_000_000)
c1.GetCardNumber
c1.DepositAmount()
c1.DepositAmount()
c1.UpdateCardNum()
c1.GetCardNumber
c1.ShowCustomerReport()
c1.GetCustomerDetails()
c1.WithdrawAmount()
c1.GetCustomerDetails()

    


