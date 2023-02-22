"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os


def bank():
    file_money = 'money.txt'
    file_orders = 'orders.txt'
    if os.path.isfile(file_money):
        with open(file_money, 'r') as f:
            money = float(f.read())
    else:
        money = 0

    lst_shop = []
    lst_m = []
    if os.path.isfile(file_orders):
        with open(file_orders, 'r') as f:
            lst = f.read().split(';')
            for orders in lst:
                if orders != '':
                    order = orders.split(':')
                    lst_shop.append(order[0])
                    lst_m.append(float(order[1]))
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            money += float(input('Введите сумму на сколько пополнить счет: '))
        elif choice == '2':
            money_shop = float(input('Введите сумму покупки: '))
            if money_shop > money:
                print('Денег не хватает')
            else:
                money -= money_shop
                lst_shop.append(input('Введите название покупки: '))
                lst_m.append(money_shop)
                print(lst_m)
        elif choice == '3':
            for i in range(len(lst_m)):
                print(lst_shop[i] + ':', lst_m[i])
        elif choice == '4':
            with open(file_money, 'w') as f:
                f.write(str(money))
            with open(file_orders, 'w') as f:
                for i in range(len(lst_m)):
                    f.write(lst_shop[i] + ':' + str(lst_m[i])+';')

            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    bank()
