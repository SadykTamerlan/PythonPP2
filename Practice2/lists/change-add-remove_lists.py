#example-1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#example-2
list = ["pp2", "calculus1", "linear algebra"]
list[1:3] = ["calculus2", "discrete structures"]
print(*list)

#example-3
thlist = ["apple", "banana", "cherry", "orange"]
thlist[1:3] = ["watermelon"]
print(thlist)

#example-4
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#example-5
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])

#example-6
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#example-7
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#example-8
slist = ["apple", "banana", "cherry"]
slist.remove("banana")
print(slist)

#example-9
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#example-10
mylist = ["brawl start", "homescapes", "clash of clans", "clash royal"]
mylist.pop()
print(mylist)

#example-11
tlist = ["duolingo", "tiktok", 1004,"instagram", "telegram", 97]
del tlist[2]
print(tlist)

#example-12
mylist = ["brawl start", "homescapes", "clash of clans", "clash royal"]
mylist.clear()
print(mylist)

#example-13
tlist = ["duolingo", "tiktok", 1004,"instagram", "telegram", 97]
del tlist
print(tlist) #error because i deleted this list