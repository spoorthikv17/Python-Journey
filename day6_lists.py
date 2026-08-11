#lists
a = [10,20,30,40,50]
print(a[0])
print(a[-1])
print(a[2:4])

#sum
print(sum(a))
sum = 0
for i in a:
    sum += i
print(sum)

#Find the largest number in a list without using max().
a = [10,20,30,40,50]
largest = a[0]
for i in a:
    if i>largest:
        largest = i
print(largest)

#Count even numbers
a = [10,20,30,40,50]
count = 0
for i in a:
    if i % 2 == 0:
        count += 1
print(count)

#Search for a number entered by the user.
numbers = [10, 20, 30, 40, 50]
user_input = int(input("Enter a number to search for: "))
for n in numbers:
    if n == user_input:
        print(f"{user_input} is found in the list.")
        break
else:
    print(f"{user_input} is not found in the list.")