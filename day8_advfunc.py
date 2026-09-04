#variable length argument
def num(*nums):
    return sum(nums)/len(nums)
print(num(2,2,2))

#recursive function
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(fact(10))

#using lambda function
mul = lambda a,b : a*b
print(mul(2,29))

#sum of n numbers
def sum(n):
    total = 0
    for i in range(0,n+1):
        total += i
    return total
print(sum(10))

#sum of n numbers using recursion
def sum(n):
    if n==0:
        return 0
    return n + sum(n-1)
print(sum(10))

