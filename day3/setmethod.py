# print set methods using for loop

s = set()

for method in dir(s):
    if not method.startswith("__"):
        print(method)