import os
import shutil
import platform
import borndayforewer
import use_functions

while True:
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Сохранить содержимое рабочей директории в файл')
    print('12. Выход')

    try:
        i = int(input('Выберите пункт: '))
        if i == 1:
            os.mkdir(input('Введите название папки: '))
        elif i == 2:
            dir_ = input('Введите название файла/папки: ')
            os.rmdir(dir_) if os.path.isdir(dir_) else os.remove(dir_)
        elif i == 3:
            dir1 = input('Введите название папки/файла: ')
            dir2 = input('Введите новое название папки/файла: ')
            shutil.copytree(dir1, dir2, False) if os.path.isdir(dir1) else shutil.copy(dir1, dir2,
                                                                                       follow_symlinks=False)
        elif i == 4:
            print(os.listdir())
        elif i == 5:
            print([dir_ for dir_ in os.listdir() if os.path.isdir(dir_)])
        elif i == 6:
            print([dir_ for dir_ in os.listdir() if os.path.isfile(dir_)])
        elif i == 7:
            print(platform.system())
        elif i == 8:
            print('Создатель программы: Alex')
        elif i == 9:
            borndayforewer.day_year('А.С.Пушкина')
        elif i == 10:
            use_functions.bank()
        elif i == 11:
            lines = 'files: '
            is_p = False
            for dir_ in os.listdir():
                if os.path.isfile(dir_):
                    if is_p:
                        lines += ', '
                    lines += dir_
                    is_p = True
            lines += '\ndirs: '
            is_p = False
            for dir_ in os.listdir():
                if os.path.isdir(dir_):
                    if is_p:
                        lines += ', '
                    lines += dir_
                    is_p = True
            with open('listdir.txt', 'w') as f:
                f.write(lines)
        elif i == 12:
            break
    except:
        print('Вы ввели не число')
