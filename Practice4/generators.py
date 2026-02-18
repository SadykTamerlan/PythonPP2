def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


#using
for number in my_range(1, 5):
    print(number)
