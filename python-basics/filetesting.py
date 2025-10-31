# Open a file and read its content

# File Handling in Python
# basic way to open a file and read its content
f = open("demofile.txt")
print(f.read())
f.close()

# Using 'with' statement to handle files
# This method automatically takes care of closing the file

with open("demofile.txt") as f:
    for line in f:
        print(line)

# Reading a Single Line
with open("demofile.txt") as f:
    print(f.readline())

# writing to a file 

# a here stands for append mode , this will add content to the end of the file
with open("demofile.txt", "a") as f:
    f.write("New Line has been added\n")

with open("demofile.txt") as f:
    print(f.read())

# Overwriting the content of a file
with open("demofile.txt", "w") as f:
    f.write("This content has overwritten the previous content.\n") 

with open("demofile.txt") as f:
    print(f.read())

# creating a new file and writing to it
with open("newfile.txt","w") as f:
    f.write("This is a newly created file.\n")
    #f.read()  # This will raise an error because the file is closed

with open("newfile.txt") as f:
    print(f.read())

# deleting a file
import os

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
    print("newfile.txt has been deleted.")
