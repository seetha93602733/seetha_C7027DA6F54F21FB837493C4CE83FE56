'
''Implement a class called BanckAcount that represents a banck account. The class should have private 
attributes for account number ,account holder name,and account balance.Include methods to
deposit money,withdraw money, and display the account balance.Ensure that the account balance 
cannot be accesssed directly from outside the class. write a program to create an instance of the 
BanckAccount class and test the deposit and withdrawal functionality.'''


class BanckAccount:
  
 def __init__(self, account_number, account_holder_name,initial_balance=0.0):
  self.__account__number = account_number
  self.__account_holder_name = account_holder_name
  self.__account_balance = initial_balance

def deposit(self, amount):
  if amount > 0:
    self.__account_balance += amount
    # self.__account_balance = self.__account_balance+amount
    print("Deposited ₹{}. New balance: ₹{}".format(amount,
                                    self.__account_balance))
  else:
    print("Invalid deposit amount. please deposit a positive amount.")
    
def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
     # self.__account_balance = self.__account_balance - amount 
      print("withdrew ₹{}. New balance: ₹{}".formate(amount,
                                        self.__account_balance))
    else:
     print("Invalid withdrawal amount or insufficiant balance.")

def display_balance(self):
  print("Account balance for {} (Account #{}): ₹{}".format(
      self.__account_holder_name, self.__account_number,
      self.__account_balance))


# create an instance of the BanckAccount class
account = BanckAccount(account_number="123456789",
                       account_holder_name="Monisha",
                       initial_balance=5000.0)

# Test deposit and withdrawal functionality 
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(2000.0)
account.display_balance()  