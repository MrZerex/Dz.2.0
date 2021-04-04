stroka = input('Введите строку: ')
spisok = stroka.split(' ')

for el in spisok:
    indx = spisok.index(el)
    if len(el) > 10:
        elemen = spisok.pop(indx)
        elemen = elemen[:10]
        spisok.insert(indx, elemen)

for ind, el in enumerate(spisok, 1):
    print(ind, el)


