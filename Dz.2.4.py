reit = [7, 5, 3, 3, 2]

while True:
    reit.reverse()
    while True:
        number = input('Введите число рейтинга: ')
        if number.isdigit() == True:
            break
        else:
            print('Необходимо ввести число')


    for num in reit:
        indx = reit.index(num)
        if num == int(number):
            reit.insert(indx, int(number))
            break
        elif reit.count(int(number)) > 0:
            continue
        else:
            reit.insert(0, int(number))
            break

    reit.reverse()
    print(f'Полученный рейтинг: {reit}')
    while True:
        again = input('Желаете продолжить? (Введите "Y" для продолжения или "N" для завершения программы): ')
        if again == 'Y':
            break
        elif again == 'N':
            break
        else:
            print('Необходимо ввести "Y" или "N"')
            continue

    if again == 'Y':
        continue
    else:
        break