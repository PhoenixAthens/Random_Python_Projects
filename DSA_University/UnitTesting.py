import unittest
from random import randint


#print(1 in range(1,2000)) # True
#print(234 in range(200, 235)) # True
#print(45 in range(50,100)) # False
listOfUsedIDS:[int] = []
class Customer:
    def __init__(self, age):
        ID_generated = randint(0,1_000_000_000)
        while ID_generated in listOfUsedIDS:
            ID_generated = randint(0,1_000_000_000)
        listOfUsedIDS.append(ID_generated)
        self.CustID = ID_generated
        self.CustAge = age
        self.creditPoints = 0


    def printCustomer(self):
        print(f"Customer ID: {self.CustID},\n Customer Age: {self.CustAge},\n Customer CP: {self.creditPoints}")

    def getAge(self):
        return self.CustAge
    def getID(self):
        return self.CustID

    def getCreditPoints(self):
        return self.creditPoints

    def setAge(self, newAge:int):
        self.CustAge = newAge

    def addCreditPoints(self, points:int):
        self.creditPoints+=points

    def offer(self, lower:int, upper:int, amt:int):
        if self.CustAge in range(lower,upper+1) and self.creditPoints == 0:
            self.creditPoints+=amt
            return True
        return False

Customer1 = Customer(25)
Customer2 = Customer(40)
Customer3 = Customer(19)
Customer4 = Customer(53)
Customer5 = Customer(18)
Customer6 = Customer(23)
custList:[Customer] = []
custList.insert(0,Customer1)
custList.insert(1,Customer2)
custList.insert(2,Customer3)
custList.insert(3,Customer4)
custList.insert(4,Customer5)
custList.insert(5,Customer6)
custList[3].addCreditPoints(50)
#print(custList)
"""
for cust in custList:
    cust.printCustomer()
    
"""

#print(listOfUsedIDS)

def test_offer(customerList):
    for customer in customerList:
        assert customer.offer(18,25,50)==True,\
        f"offer failed on customer: {customer.CustID} because age: {customer.CustAge}"


#test_offer(custList)

"""
The program works even if we run our program simple by just calling the function:
However since "Customer2" has age 40, our assertion fails and we get the following error:

Traceback (most recent call last):
  File "/Users/anmolkhanna/Downloads/To push On GIT/Python Projects/DSA_University/UnitTesting.py", line 65, in <module>
    test_offer()
  File "/Users/anmolkhanna/Downloads/To push On GIT/Python Projects/DSA_University/UnitTesting.py", line 62, in test_offer
    assert customer.offer(18,25,50)==True,\
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: offer failed on customer: 571979709 because age: 40
"""
listOfCustomer:[Customer] = []
listOfCustomer.insert(0,Customer(18))
listOfCustomer.insert(1,Customer(23))
custList[1].addCreditPoints(50)
listOfCustomer.insert(2,Customer(25))
listOfCustomer.insert(3,Customer(53))

test_offer(listOfCustomer)
"""
Above call gives us the following error:

Traceback (most recent call last):
  File "/Users/anmolkhanna/Downloads/To push On GIT/Python Projects/DSA_University/UnitTesting.py", line 89, in <module>
    test_offer(listOfCustomer)
  File "/Users/anmolkhanna/Downloads/To push On GIT/Python Projects/DSA_University/UnitTesting.py", line 65, in test_offer
    assert customer.offer(18,25,50)==True,\
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: offer failed on customer: 931286950 because age: 53
"""

if __name__ == '__main__':
    unittest.main()



# to run program from command line, use "python3 -m unittest <fileName.py>"