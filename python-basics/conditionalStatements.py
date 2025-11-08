# Conditional statements using If block in python

a = 5

if a == 10:
    print("A is assigned to your number")
else:
    print("A is not assigned to your favourite number")


# Using elif block to check the condition multiple times

a = 40
b = 40

if a > b:
    print("A is greater")
elif a == b:
    print("A and B are both equal")
else:
    print("B is greater than A")



# Categorizing the age

age = 30

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age <= 30:
    print("you are an adult")
else:
    print("you are old")


# Categoring the days of the week 

day = 6

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")

# else statement
# Else statement will act as catch all block

temp = 31

if temp > 30:
    print("Its hot outside")
elif temp > 20:
    print("Its pleasant")
else:
    print("Its cold")



name = ""

if len(name) > 0:
    print(f"welcome, {name}!")
else:
    print("Username cannot be empty")


# Short hand if Statments

a = 1

if a == 1:print("A is equals to one")


a = 20
b = 200

print("A") if a > b else print("B")


# Ternary Operators in Python

a = 600
b = 900

# Here the  bigger is getting assigned with the out of the tenary operator
bigger = a if a > b else b
print("Bigger is ", bigger)


