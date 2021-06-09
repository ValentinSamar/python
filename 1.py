new_list = ['seven', 7, 7.7, True, False, (5, 6, 7, 8), [5, 7, 8, 3], {6, 5, 4, 9}]
for i, item in enumerate(new_list, 1):
    print(f"{i}. {item}-{type(item)}")
