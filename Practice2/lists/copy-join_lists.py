#example-1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#example-2
thislist = ["brawl start", "homescapes", "clash of clans", "clash royal"]
mylist = list(thislist)
print(mylist)

#example-3
thislist = ["duolingo", "tiktok", 1004,"instagram", "telegram", 97]
mylist = thislist[:]
print(mylist)

#example-4
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#example-5
list1 = ["chanel", "dior", "hermes", "cartier"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#example-6
list1 = ["burger", "doner", "sandwich"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)