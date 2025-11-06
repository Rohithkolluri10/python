
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
