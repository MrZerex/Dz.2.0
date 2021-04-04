#Решение списком

mounths = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9 ,10, 11]]

while True:
    mounth = int(input('Введите номер месяца (от 1 до 12): '))
    if mounth > 12 or mounth < 1:
        print('Такого месяца нет')
    else:
        break

for el in mounths:
    indx = mounths.index(el)
    for em in el:
        if em == mounth:
            if indx == 0:
                print('Это месяц зимы')
            elif indx == 1:
                print('Это месяц весны')
            elif indx == 2:
                print('Это месяц лета')
            else:
                print('Это месяц осени')

#Решение словарем
#mounths = {
#    (12, 1, 2) : 'Зима',
#    (3, 4, 5) : 'Весна',
#    (6, 7, 8) : 'Лето',
#    (9, 10, 11) : 'Осень'
#}
#
#while True:
#    mounth = int(input('Введите номер месяца (от 1 до 12): '))
#    if mounth > 12 or mounth < 1:
#        print('Такого месяца нет')
#    else:
#        break
#
#for el in mounths.keys():
#    for em in el:
#        if mounth == em:
#            print(mounths.get(el))
#