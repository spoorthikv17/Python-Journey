#reverse a string
a = ["h","e","l","l","o"]
print(a[::-1])

a = "A man, a plan, a canal: Panama"
a = ''.join([i for i in a if i.isalnum()]).lower()
a.lower()
b = a[::-1]
if a==b:
    print("True")
else:
    print("False")
