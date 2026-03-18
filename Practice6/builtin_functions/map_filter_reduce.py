from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map(): square numbers
squared = list(map(lambda x: x**2, numbers))

# filter(): get even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))

# reduce(): sum of numbers
total = reduce(lambda x, y: x + y, numbers)

print("Squared:", squared)
print("Even:", even)
print("Sum:", total)