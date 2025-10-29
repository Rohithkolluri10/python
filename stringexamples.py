print("Hello, World!")
print("this is a simple 'Python' script.")
print('this is another line with "double quotes".')


a = 'something'
print(a)

testing_multiple_lines = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""

print(testing_multiple_lines)

print(a[3])
print(a[-1])

for char in a:
    print(char)

print(len(testing_multiple_lines))

print( "ut" in testing_multiple_lines )
print( "ipsum" in testing_multiple_lines )

print( "something" not in testing_multiple_lines )

if "dolor" in testing_multiple_lines:
    print("Found it!")
else:
    print("Not found.")


if "hello" not in testing_multiple_lines:
    print("Hello is not there.")
else:
    print("Hello is there.")


string_slicing = "abcdefghij"
print(string_slicing[2:5])

print(string_slicing[:3])
print(string_slicing[3:])

print(string_slicing[-5:-1])

print(string_slicing.upper())

_string_formatting = "ABCDEFGHIJKLM"

print(_string_formatting.lower())


testing_strip = "    Hello, World!    "
print(testing_strip.strip())

testing_replace = "Hello, World!"
print(testing_replace.replace("o","0"))
print(testing_replace.replace("World","Universe"))

testing_split = "Hello, World!"
print(testing_split.split(","))


a = "Hello"
b = "World"
c = a + b
print(c)
d = a + " " + b
print(d)