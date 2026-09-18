nums = [ 2 , 123 , 234 , 2223]
ans = []

for i in nums:
    if len(str(i)) % 2 == 0:
        ans.append(i)

print(len(ans))
