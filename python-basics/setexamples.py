
myset = {"name", 42 , 28.1, "email", True, 1}
myfalseSet = {"name", 42, 28.1,"email", False, 0}
mySetConstructor = set(("Name", True, 1 , 0 , False))


print(mySetConstructor)
print(myset)
print(myfalseSet)
print(len(myfalseSet))
print(type(myset))

# looping through sets
for x in myset:
    if x == 42:
        print(x)


# Adding items to a set

testset = {"this", "testing", "set","available"}
testset.add("added")
print(testset)

combiningtwosets = {"another", "test" , "items"}
testset.update(combiningtwosets)
print(testset)

adding_list_set = ["Hello", "Hello", True , 1]
testset.update(adding_list_set)
print(testset)

# remove method
testset.remove("Hello")
# Discard method
testset.discard(True)
# pop method
testset.pop()
#  clear method
del testset


set1 = {1,2,3,4,5}
set2 = {"a","b","c","d","e"}
set3 = {"name","email", "address"}

set4 = set1.union(set1,set2,set3)
print(set4)

set5 = {"Something","has","added"}

set6 = set4 | set5
print(set6)