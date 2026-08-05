#print from 0 to 10
for i in range(0 , 11):
    print(i , end = " ")

#print from 10 to 0
for i in range(10 , -1 ,-1):
    print(i)

for i in range( 0 ,50 ,2):  #if i start from 0 and increment by 2 then it will print even numbers
    print(i , end = " ")

for i in range( 1 ,50 ,2):  #if i start from 1 and increment by 2 then it will print odd numbers
    print(i , end = " ")

a = int(input("Enter a number to print its multiplication table: "))
for i in range(1 , 11 , 1):
    b = a * i
    print(a , "x" , i , "=" , b)