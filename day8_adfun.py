#mixed 
def square_sum(*args):
    a = []
    square = lambda x: x**2

    for x in args:
        a.append(square(x))

    return sum(a)

print(square_sum(2, 3))

#running sum 
def runn_sum(n):
    tot = 0
    a = []
    for i in range(len(n)):
        tot += n[i]
        a.append(tot)
    return a
print(runn_sum([1, 2, 3, 4, 5]))

#finding two sum
def two_sum(nums, target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([2, 7, 11, 15], 109))