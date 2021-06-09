n = input("Введите эменты, разделяя их пробелами-").split()
i = 0
print(f'Изначальный список{n}')
while i + 1 < len(n):
    if i % 2 == 0:
        n.insert(i, n.pop(i + 1))
    i += 1
print(f'Измененый список{n}')
