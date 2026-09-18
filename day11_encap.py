#Encapsulation
class Student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks #private variable

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks
    
s = Student("Spoo",50)
print(s.get_name())
print(s.get_marks())

#Bank account
class BankAccount:
    def __init__(self,amount,balance):
        self.__amount = amount
        self.__balance = balance

    def add_amount(self,amount):
        self.__amount = amount
        self.__balance += amount

    def get_balance(self):
        return self.__balance

s = BankAccount(1000,5000)
s.add_amount(5000000000000)
print(s.get_balance())