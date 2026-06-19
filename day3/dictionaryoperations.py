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
print("Country (missing key):")
print(student.get("country", "Not found"))

# length and membership
print("\nLength:", len(student))
print("Does 'age' exist?", "age" in student)
print("Does 'city' exist?", "city" in student)

# add new key with assignment
student["grade"] = "A"
print("\nAfter adding grade:")
print(student)

# update()
student.update({"marks": 90, "course": "Python Basics"})
print("After update:")
print(student)

# pop()
removed_age = student.pop("age")
print("\nPopped age:", removed_age)
print("After pop:")
print(student)

# popitem()
popped_item = student.popitem()
print("\nPopped item:", popped_item)
print("After popitem:")
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