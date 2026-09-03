#simple calcualte_fahrrenheit
def calculate_fah(cel):
    return (cel*9/5)+32
fah = calculate_fah(32)
fah = calculate_fah(0)
print(fah)

#greet user with default value
def greet_user(name , greeting="hello"):
    print(f"{greeting} {name}")
    print(f"hii {name} , welcome to python programming")
greet_user("spoo")
greet_user("spoo", "hi")

#max function
def find_max(a, b, c):
    return max(a, b, c)
print(find_max(10, 20, 30))

#max
def max_num(numbers):
    if not numbers:
        return None
    
    max_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
print(max_num([10,2,3,4]))