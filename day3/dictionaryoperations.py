# Dictionary methods program

student = {
    "name": "Nikitha",
    "age": 20,
    "course": "Python"
}

print("Original dictionary:")
print(student)

# keys()
print("\nKeys:")
print(student.keys())

# values()
print("Values:")
print(student.values())

# items()
print("Items:")
print(student.items())

# get()
print("Name:")
print(student.get("name"))

# update()
student.update({"marks": 90})
print("After update:")
print(student)

# pop()
student.pop("age")
print("After pop:")
print(student)

# copy()
new_dict = student.copy()
print("Copied dictionary:")
print(new_dict)

# setdefault()
student.setdefault("city", "Hyderabad")
print("After setdefault:")
print(student)

#fromkeys()
keys = ["id", "name", "branch"]
new_student = dict.fromkeys(keys, "NA")
print("Using fromkeys:")
print(new_student)

# clear()
new_dict.clear()
print("After clear:")
print(new_dict)