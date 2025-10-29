# Intro into the string formatting methods in Python

# name = "rohith"
# age = 25
# print(name + age)

# above code will give type error because we are trying to concatenate string and integer

# to avoid that we can use string formatting methods

# String Formatting using f-strings and was introduced Python 3.6+

name = "rohith"
age = 25
print(f"my name is {name} and my age is {age}")

age = 20
print(f"my name is Rohith and age is {age}")

# In the above example {} is a placeholder

# We can use operations inside the placeholders, and also call functions and modifiers

# example of a operation inside the placeholder
number = 10
print(f"the square of {number} is {number **2}")

# example 2 of operation inside the placeholder
length = 5
width = 10
print(f"Are of a rectangle is {length * width}")

# example of function inside the placeholder
name = "rohith"
print(f"My name in uppercase is {name.upper()}")

# example of modifier inside the placeholder
# Collen (:) is used to separate the variable and the modifier
# .2f is used to format a floating point number to 2 decimal places
pi = 3.141592653589793
print(f"The value of pi up to 3 decimal places is {pi:.2f}")

# Another example of modifier with percentage
percentage = 0.7567
print(f"The percentage is {percentage:.2%}")


