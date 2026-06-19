main_list = []

for i in range(3):
    sub_list = []
    for j in range(3):
        sub_list.append(j)
    main_list.append(sub_list)

print(main_list)
list1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

total = 0

for i in list1:
    for j in i:
        total = total + j

print("Addition =", total)