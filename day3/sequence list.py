list_methods = []

for method in dir(list):
    if not method.startswith("__"):
        list_methods.append(method)

print(list_methods)