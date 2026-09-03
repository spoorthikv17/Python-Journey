#greet function
def greet():
    print("HEllo,I'm spoorthi")
greet()

#parameterized greeting
def greet(name):
    print(f"Hii {name} , heartly welcome u")
greet("Spooo")

#sum function
def add_sum(a,b):
    return a+b
c = add_sum(50,20)
print(c)

def add_sum(a,b):
    print(f"{a} + {b}")
add_sum(20,20)