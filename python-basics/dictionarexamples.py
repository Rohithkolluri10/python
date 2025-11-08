
mydict = {
    "name": "Mustang",
    "make": "ford",
    "model": 1995
}

print(mydict)
print(mydict["make"])


dict_With_types = {
    "name": "Mustang",
    "make": "Ford",
    "electric": False,
    "color": ["Red","Black","Blue"],
    "year": 1964 
}

print(dict_With_types)
print(len(dict_With_types))
print(type(dict_With_types))


# accessing the dict with a keys

# access items with keys
# access items with values

print(dict_With_types.keys())
print(dict_With_types.values())
dict_With_types["make"] = "Mercedes"
print(dict_With_types.keys())
print(dict_With_types.values())

# The items() method will return each item in a dictionary, as tuples in a list.

x = dict_With_types.items()

print(x)

dict_With_types["color"] = "Brown"

print(x)

if "make" in dict_With_types:
  print("Yes the model is present in the dict")

# Using Update Method in the dict
# The argument must be a dictionary, or an iterable object with key:value pairs

dict_With_types.update({"make":"Suzuki"})
print(dict_With_types)

# Removing items from the dictionay
# dict_With_types.pop("make")
# print(dict_With_types)

# popitem() will remove the last item in the dictionary

# dict_With_types.popitem()
# print(dict_With_types)

# clear will empties the dict

# dict_With_types.clear()
# print(dict_With_types)

# del keyword will entirely delete the dict

# looing through dictionaries 

for x in dict_With_types:
    print(x)

for x in dict_With_types:
    print(dict_With_types[x])


for x in dict_With_types.values():
    print(x)

for x,y in dict_With_types.items():
    print(x,y)

# Copying the Dictionary , We cannot copy traditionally using + symbol.

# we can use copy metho or the dict keyword

mydict_prep = dict_With_types.copy()
print(mydict_prep)

my_dict_prep_always = dict(dict_With_types)
print(dict_With_types)

# Nested Dictionaries

# Contains Dictionaries within dictionary

myfamily = {
    "child1" : {
        "name": "emily",
        "year": 2004
    },

    "child2": {
        "name": "tobias",
        "year": 2005
    },

    "child3": {
        "name": "linux",
        "Year": 2007
    }
}

print(myfamily)

# we can also create three dict individually and add it to new dict

friend1 = {
    "name": "Deekshith",
    "Area": "Dharmaram"
}

friend2 = {
    "name": "Kalyan",
    "Area": "Labour colony"
}

friend3 = {
    "name": "Akhil",
    "Area": "Geesukonda"
}

friends_dict = {
    "friend1": friend1,
    "friend2": friend2,
    "friend3": friend3
}

print(friends_dict["friend3"]["Area"])

for x, obj in friends_dict.items():
    print(x)
    for y in obj:
        print(y + ":", obj[y])
