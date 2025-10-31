
# This is an example of a tuple in Python

# Tuple are immutable sequences, means they cannot be changed after creation

# Tuple are indexed, allowing access to elements via their position

tupleexample = (1, 2, 3, 4, 5)

# creating a sigle element tuple
# important: include a comma after the single element
single_element_tuple = (1,)

print("Tuple Example:", tupleexample)
print(f"Single Element Tuple: {single_element_tuple}")


tuplewithStrings = ("apple", "banana", "cherry")
print(tuplewithStrings[0])

# Tuples can contain mixed data types
mixed_tuple = (1, "hello", 3.14, True)
print("Mixed Tuple:", mixed_tuple)

# Tuples support unpacking
a, b, c, d, e = tupleexample
print("Unpacked Values:", a, b, c, d, e)

# As Tuples are immutable, we cannot add or remove elements directly
# However, we can convert a tuple to a list, modify it, and convert it back
tupleconvert = list(tupleexample)
tupleconvert.append(6)
new_tuple = tuple(tupleconvert)
print("New Tuple after conversion and modification:", new_tuple)

# Tuple unpacking with asterisk (*) to capture remaining elements


fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# looping through a tuple

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "strawberry", "raspberry")

for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(fruits[i])

# loop with break statement
for x in fruits:
    if x == "banana":
        break
    print(x)


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# joining two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# multiplying tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)