class Employee:
    def __init__(self, name, designation , salary = 30000):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Designation: {self.designation}, Salary: {self.salary}")

emp1 = Employee("spoo","HR")
emp1.display_info()
emp2 = Employee("Darshu","Manager",50000)
emp2.display_info()