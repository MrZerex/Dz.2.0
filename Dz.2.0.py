spisok = [18, 19.3, 'stroka', True, None]
print(f'Дан список: {spisok}')
indx = 1

for el in spisok:
    print(f'Элемент {indx} имеет тип {type(el)}')
    indx += 1