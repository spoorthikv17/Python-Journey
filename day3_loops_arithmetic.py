# Arithmetic Operations with Loops
#Find the sum of numbers from 1 to n.
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of numbers from 1 to", n, "is", sum)

#Find the factorial of a number.
n = int(input("Enter a number to find its factorial: "))
sum = 1 
for i in range(1, n + 1):
    sum *= i
print("The factorial of", n, "is", sum)

#Count how many digits are present in a number.
n = int(input("Enter a number to count its digits: "))
count = 0
for i in range(len(str(n))):
    count += 1
print("The number of digits in", n, "is", count)

