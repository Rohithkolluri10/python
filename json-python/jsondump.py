import json

# creating a python object which is a Dictionary

python_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Python", "Data Science"]
}

# Serialize 
# Convert a python object to a json formatted String

json_dict = json.dumps(python_dict, indent=4)

print("________Printing Python Json Module_______________")
print(python_dict)
print(json_dict)