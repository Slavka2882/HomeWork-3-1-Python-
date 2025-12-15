lst = [1, 2, 3, 4, 5]

if len(lst) == 0:
    new_list = [[], []]
else:
    middle = (len(lst) + 1) // 2
    new_list = [lst[:middle], lst[middle:]]

print(new_list)
