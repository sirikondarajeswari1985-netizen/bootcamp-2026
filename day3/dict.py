# print dictionary methods using for loop

d = {}

for method in dir(d):
    if not method.startswith("__"):
        print(method)