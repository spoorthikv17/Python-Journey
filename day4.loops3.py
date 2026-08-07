# Print all numbers between 1 and 100 that are divisible by both 3 and 5.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#Count how many even numbers are there between 1 and 100.
count = 0
for i in range(1, 101):
    if i % 2 == 0:
        count += 1
print(count)

#Count how many odd numbers are there between 1 and 100.
count = 0
for i in range(1, 101):
    if i % 2 != 0:
        count += 1
print(count)

for i in range(1 , 6):
    for j in range(i):
        print("*", i, j)

