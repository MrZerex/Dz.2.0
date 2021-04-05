tovar = dict()
kol = 1
spisok = []
katalog = []
while True:
    naimen = input('Введите характеристику товара (для завершения ввода характеристик введите "!",'
                   ' для создания нового товара введите "!!"): ')
    if naimen == '!':
        tovarcopy = tovar.copy()
        tovar.clear()
        spisok.append(kol)
        spisok.append(tovarcopy)
        spisok = tuple(spisok)
        katalog.append(spisok)
        break
    elif naimen == '!!':
        tovarcopy = tovar.copy()
        tovar.clear()
        spisok.append(kol)
        spisok.append(tovarcopy)
        kol += 1
        spisok = tuple(spisok)
        katalog.append(spisok)
        print(katalog)
        spisok = list(spisok)
        spisok.clear()
        continue


    znach = input('Введите значение характеристики товара: ')
    tovar[naimen] = znach

print(katalog)
