reit = [7, 5, 3, 3, 3, 2, 5, 3, 3, 3, 2, 1]
new_number = int(input('Введите новый элемент рейтига в виде натурального числа - '))
i = 0

for n in reit:
    if new_number <= n:
        i += 1
reit.insert(i, float(new_number))
print(reit)
