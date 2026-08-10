#strings
a = "Python"
b = "Programming"
print(a[0])
print(a[-1])

#Count characters
print(len(a))
print(a.count("o"))

#Vowels
a = "Python"
vowels = "aeiouAEIOU"
print(a.count(vowels))

#Take a string and print it in reverse.
a = "Python"
print(a[::-1])

#Check whether a string is a palindrome.
a = "madam"
b = a[::-1]
if a==b:
    print("Palindrome")
else:
    print("Not a palindrome")