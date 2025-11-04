# Collections in python: Lists

# A list is a collection which is ordered and changeable. Allows duplicate members.

# creating a list

mylist = ["apple", "banana","cherry"]
print(mylist)

# Accessing the items in the list

# indexing starts from 0
print(mylist[0])
print(mylist[1])
print(mylist[2])

# negative indexing
print(mylist[-1])  # last item
print(mylist[-2])  # second last item
print(mylist[-3])  # third last item

# Range of indexes
print(mylist[1:3])  # from index 1 to index 2
print(mylist[:2])   # from start to index 1
print(mylist[1:])   # from index 1 to end

for item in mylist:
    print(item)

# Checking if an item exists in the list

# Using the variable in the loop
item = "banana"
if item in mylist:
    print(f"Yes, '{item}' is in the list.")
else:
    print("No, '{item}' is not in the list.".format(item=item))


print(mylist)

mylist[1] = "orange"
print(mylist)

mylist[1:3] = ["blackcurrant", "vanilla"]

print(mylist)

mylist.insert(2, "watermelon")
print(mylist)

mylist.append("kiwi")
print(mylist)

mytuple = ("mango", "pineapple")
mylist.extend(mytuple)
print(mylist)

i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1
print(mylist)



# list Comprehension
squares = [x**2 for x in range(10)]
print(squares)

#understanding the list Comprehension

additioninrange = [ x + 2 for x in range(10)]
print(additioninrange)


primenumbersinlist = [ x % 2 !=0 for x in range(10)]
print(primenumbersinlist)


mytestlist = ["rohith", "gauthami","mummy","daddy","gudi"]
newlist = [x.upper() for x in mytestlist if "mummy" in x]
print(newlist)



# sorting a list
sortlist = ["orange", "mango", "kiwi", "pineapple", "banana"]
sortlist.sort()
print(sortlist)

# reversing a list
sortlist.reverse()
print(sortlist)

# Sorting a number list

numberlistsort = [100, 50, 65, 82, 23]
numberlistsort.reverse()
newlist_forcopying = numberlistsort.copy()
copyingthroughconstructor = list(newlist_forcopying)
copyingthroughsliceoperation = copyingthroughconstructor[:]
print(numberlistsort)
print(newlist_forcopying)
print(copyingthroughconstructor)
print(copyingthroughsliceoperation)