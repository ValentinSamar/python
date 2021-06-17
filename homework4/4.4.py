from random import randint

per = [randint(-10, 10) for _ in range(20)]
spis = [el for el in per if per.count(el) == 1]
print(f'Начальный спиок\n{per}\nСписок без повторений\n{spis}')


print(a := [randint(0, 9) for j in range(20)], '\n', [i for i in a if a.count(i) == 1], sep="")