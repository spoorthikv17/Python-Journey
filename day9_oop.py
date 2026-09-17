class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def mobile_det(self):
        print(f"I bought a phn and its brand is {self.brand}")
        print(f"And the price is {self.price}")

mob = Mobile("Iphone",10000)
mob.mobile_det()

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"My name is {self.name} and I scored {self.marks} marks in my exam")

stud1 = student("Spoo",50)
stud2 = student("Darshu",100)
stud1.display_info()
stud2.display_info()
