spisok = []

while True:
    element = input('Введите элемент списка (если элементов достаточно, введите "!"): ')
    if element == '!':
        break
    else:
        spisok.append(element)

print(f'Исходный список: {spisok}')

for elem in spisok:
    indx = spisok.index(elem)
    if indx % 2 != 0:
        el = spisok.pop(indx)
        spisok.insert(indx - 1, el)

print(f'Получившийся список: {spisok}')