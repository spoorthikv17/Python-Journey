#Take a number as input and check whether it is positive, negative, or zero
a = int(input("enter a number: "))
if a > 0:
    print("The number is positive")
elif a<0 :
    print("The number is negative")
else:
    print("The number is zero")

#Take a number and check whether it is even or odd.
b = int(input("enter a number: "))
if b % 2==0:
    print("The number is even")
else:
    print("The number is odd")

#Take two numbers and print the greater number.
a = int(input("enter first number: "))
b = int(input("enter second number: "))
if a > b:
    print("The greater number is", a)
else:
    print("The greater number is", b)

#Take three numbers and print the greatest number.
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
if a > b and a > c:
    print("The greatest number is", a)
elif b > c:
    print("The greatest number is", b)
else:
    print("The greatest number is", c)

#students marks 
marks = int(input("enter your marks: "))
if marks >= 90 and marks<=100:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
else:
    print("Grade D")