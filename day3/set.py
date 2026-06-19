# create a set
s = {10, 20, 30, 40}

print("Original set:", s)

# add()
s.add(50)
print("After add:", s)

# update()
s.update([60, 70])
print("After update:", s)

# remove()
s.remove(20)
print("After remove:", s)

# discard()
s.discard(100)   # no error if element not present
print("After discard:", s)

# pop()
x = s.pop()
print("Removed element:", x)
print("After pop:", s)

# copy()
s2 = s.copy()
print("Copied set:", s2)

# clear()
s2.clear()
print("After clear:", s2)
# two sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

# Union (all elements from both sets)
print("Union:", set1.union(set2))
print("Union using | :", set1 | set2)

# Intersection (common elements)
print("Intersection:", set1.intersection(set2))
print("Intersection using & :", set1 & set2)

# Difference (elements only in first set)
print("Difference:", set1.difference(set2))
print("Difference using - :", set1 - set2)

# Symmetric difference (not common elements)
print("Symmetric difference:", set1.symmetric_difference(set2))
print("Using ^ :", set1 ^ set2)

# Subset
a = {10,20}
print("Subset:", a.issubset(set1))

# Superset
print("Superset:", set1.issuperset(a))