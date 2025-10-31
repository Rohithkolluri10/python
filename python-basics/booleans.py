# Booleans in Python
# Booleans represent one of two values: True or False.
is_raining = True
is_sunny = False
print("Is it raining?", is_raining)
print("Is it sunny?", is_sunny)

print(10 > 5)  # True
print(10 < 5)  # False
print(10 == 9)  # True
# here == is used to compare values for equality not assignment

# Using booleans in conditional statements

a = 10
b = 5

if a > b: # this evaluates to True
    print("a is greater than b") # this block runs because the condition is True
else: 
    print("a is not greater than b") # this block has been skipped as the first condition is True


# boolean functions will evaluate to either True or False
# Any values can be evaluated in a boolean context using the bool() function will be true expect empty zero or None

# Any number is True, except 0
print(bool(1))  # True
print(bool(0))  # False

# Any string is True, except empty strings.
print(bool("Hello"))  # True
print(bool(""))       # False

# Any list, tuple, set, and dictionary are True, except empty ones.
print(bool([1,2,3])) # True
print(bool([])) # false

# tuple

print(bool((1,2))) # true
print(bool(())) # false

# set
print(bool({1,2})) # true
print(bool(set())) # false

# dictionary
print(bool({"key": "value"})) # true
print(bool({})) # false


# Example: Using a boolean function to check if a number is even or odd

def is_even(number):
    """Function to check if a number is even."""
    return number % 2 == 0  # returns True if even, False if odd

# Testing the function
a = 3
if is_even(a):
    print(f"{a} is even")
else:
    print(f"{a} is odd")