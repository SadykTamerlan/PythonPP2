#1
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#2
def my_func(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

my_func("Sezim", "Aizere", "Merey")

#3
def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Madina", "Mingyu", "Yasmina")

#4
def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#5
def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(my_function(3, 7, 2, 9, 1))

#6
def my_function(**kid):
    print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")

#7
def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

#8
def my_function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

#9
def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function("User Info", "Turgynbek", "Madina", age = 17, city = "Taraz")

#10
def my_function(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) 
print(result)

#11
def my_function(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)

#12
def sum(*nums):
    total = 0
    for numbers in nums:
        total += numbers
    
    return total

numbers = {1, 2, 3, 4, 5, 6}
print(sum(*numbers))

#13
def find_max(*numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    
    return max

numbers = {-99, 258, 115, 97, 208, 45}
print(find_max(*numbers))

#14
def count_even(*nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count
        

nums = {2, 78, 19, 97, 5, 11}
print(count_even(*nums))

#15
def user_info(**user):
    print("Name: ", user["name"])
    print("Age: ", user["age"])
    print("City: ", user["city"])

user_info(name = "Madina", age = 17, city = "Taraz")

#16
def calculate_total_price(**products):
    total_sum = 0
    for p in products:
        total_sum += products[p]
    return total_sum

print(calculate_total_price(apple=300, banana=200))