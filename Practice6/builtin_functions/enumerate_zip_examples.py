names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 88]

# enumerate(): index + value
for i, name in enumerate(names):
    print(i, name)

# zip(): combine two lists
for name, score in zip(names, scores):
    print(name, score)

# type checking and conversion
value = "100"

if isinstance(value, str):
    number = int(value)
    print("Converted:", number, type(number))