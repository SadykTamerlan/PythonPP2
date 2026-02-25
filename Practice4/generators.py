# Generator that generates squares up to N
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2


           # Example usage
for value in square_generator(5):
    print(value)


# Generator to print even numbers between 0 and n (comma separated)
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


n = int(input("Enter n: "))

print(",".join(str(num) for num in even_numbers(n)))

#Generator for numbers divisible by 3 and 4 between 0 and n

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input("Enter n: "))

for num in divisible_by_3_and_4(n):
    print(num)

#Generator squares(a, b) from a to b

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


          # Test
for value in squares(3, 7):
    print(value)

#Generator from n down to 0

def countdown(n):
    while n >= 0:
        yield n
        n -= 1


# Example usage
for number in countdown(5):
    print(number)