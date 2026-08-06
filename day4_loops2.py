#reversing a digit
number = int(input("Enter a number: "))
reverse = 0
while number > 0:
    digit = number % 10  #get the last digit
    reverse = reverse * 10 + digit #remove the last digit and add it to the reverse
    number = number // 10 #remove the last digit
print("The reverse of the number is:", reverse)

#palindrome
number = int(input("enter a number:"))
original_num = number 
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse *10 + digit
    number = number //10
if original_num == reverse:
    print(original_num, "is a palindrome")
else:
    print(original_num, "is not a palindrome")

#finding the largest digit in a number
number = int(input("Enter a number: "))
largest_digit = 0
while number > 0:
    digit = number %10
    number = number// 10
    if digit > largest_digit:
        largest_digit = digit
print("The largest digit in the number is:", largest_digit)

#sum of digits in a number
number = int(input("Enter a number: "))
sum = 0 
while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10
print("The sum of the digits in the number is:", sum)

# even or odd number of digits in a number
number = int(input("Enter a number: "))
count = 0
while number > 0:
    digit = number % 10
    count += 1
    number = number//10
if count % 2 == 0:
    print("The number has an even number of digits")
else:
    print("The number has an odd number of digits")

#factors of a number
number = int(input("Enter a number: "))
print("The factors of", number, "are:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)