#1
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#2
def func(uni):
    print("I study at university " + uni)

uni = "KBTU"
func(uni)

#3
def my_function(name): # name is a parameter
    print("Hello", name)

my_function("Mdin") # "Mdin" is an argument

#4
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")

#5
def my_function(country = "Norway"):
    print("I am from", country)

my_function("Sweden")
my_function("Kazakhstan")
my_function()
my_function("Brazil")