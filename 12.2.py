'''
создать персонажей на базе родительского класса, путем наследования основых атрибутов и методов,
 так же добавиьт свои методы
'''
import json
import time
from Cheractor import *


class Decor:  # создаем декоратор, для замера времени работы функции
    def __init__(self, funk):
        self.funk = funk

    def __call__(self, n):
        s = time.time()
        self.funk(n)
        f = time.time()
        print(f' Время выполнения функции :{f - s}')


class MyErr(Exception):  # создаемсобвстенное  исключение
    pass


class Voin(Cheractor):
    # создаем клас воин, которые включает в себя свойства, описанные ниже

    def __init__(self, nik, rasa, pol, color_yeas, tip_vneshnosti, zdorovie,
                 basovi_uron):  # конструктор создания классов и их методов

        super().__init__(nik, rasa, pol, color_yeas, tip_vneshnosti, zdorovie, basovi_uron)  # наследование в родителя

    def ydar_me4em(self):  # создаем метод с одноименным названием
        return 'удар мечом - наносит 2 урона'

    def ydar_shitom(self):  # создаем метод с одноименным названием
        return ' удар щитом – наносит 1 урон'

    def info_2(self):  # наследуем методы
        super().info_sup()

    def zdorov_2(self):  # наследуем методы
        super().ischelenie()


# устраиваем диалог с пользователем
nik = input('Введите имя персонажа :')
ras = input('введите расу :')
pol = input('введите пол персонажа :')
color_yeas = input('введите цвет глаз :')
tip_vneshnosti = input('введите тип внешности :')
# обрабатываем исключения
try:
    zdorovie = int(input('Введите здоровье :'))

except:
    zdorovie = int(input('Введите здоровье цифрами :'))
try:
    basovi_uron = int(input('Введите базовый урон :'))
except:
    basovi_uron = int(input('Введите базовый урон цифрой :'))


# def __del__(self): деструктор для удаления обьектов


class Mag(Cheractor):  # создае класс на основе родительского

    def __init__(self, nik, rasa, pol, color_yeas, tip_vneshnosti, zdorovie,
                 basovi_uron, ):  # конструктор создания классов и их методов

        Cheractor.__init__(self, nik, rasa, pol, color_yeas, tip_vneshnosti, zdorovie, basovi_uron)

    def ogneni_shar(self):  # создаем метод с одноименным названием
        return 'огненный шар - наносит 5 урона и произносится 5 секунд'

    def freez(selfs):  # создаем метод с одноименным названием
        return 'заморозка – наносит 1 урона'

    def info_2(self):
        super().info_sup()

    def zdorov_2(self):
        return super().ischelenie()


class Charodei(Voin, Mag):  # создаем класс путем множественного наследования
    def __init__(self, nik, rasa, pol, color_yeas, tip_vneshnosti, zdorovie, basovi_uron):
        Voin.__init__(self, nik, rasa, pol, color_yeas, tip_vneshnosti, zdorovie,
                      basovi_uron)  # наследуем у класса воин

    def ydar_ognem(self):  # наследуем у класса маг
        Mag.ogneni_shar(self)

    def ydar(self):  # наследуем у класса  воин
        Voin.ydar_shitom(self)

    def zamedlenie(self):
        return 'Замедляет на -2'

    def info_char(self):
        Mag.info_2()


a = input('выберите класс : воин, маг или чародей ')
# далее проверка на типп персонажа, если выбирается маг, то создается обьект класа Mag и свойтсвами класа Mag
# выбирает  воин, то создается отбьек класа Voin, свойствами класа Voin
if a == 'маг':
    pers = Mag(nik, ras, pol, color_yeas, tip_vneshnosti, zdorovie, basovi_uron)
    if pers.zdorovie < 4:
        raise MyErr('создайте персонажа с большем здоровьем')
    print(pers.info_2())  # выводим метод инфо

    # выводим все методы класа Mag
    print(f'У мага есть умения :  {pers.ogneni_shar()} + базовый урон наносит {pers.basovi_uron},'
          f' {pers.freez()} + базовый урон наносит {pers.basovi_uron}')
    print(pers.zdorov_2())



elif a == 'воин':
    pers = Voin(nik, ras, pol, color_yeas, tip_vneshnosti, zdorovie, basovi_uron)
    print(pers.info_2())

    # выводим все методы класа Voin
    print(f'У воина есть умения:  {pers.ydar_me4em()} + базовый урон наносит {pers.basovi_uron} , '
          f'{pers.ydar_shitom()} + базовый урон наносит {pers.basovi_uron}')
    print(pers.zdorov_2())

elif a == 'чародей':
    pers = Charodei(nik, ras, pol, color_yeas, tip_vneshnosti, zdorovie, basovi_uron)
    print(pers.info_2())
    print(f'У чародея есть сладующие умения : {pers.ydar_shitom()}+ базовый урон наносит {pers.basovi_uron}, '
          f', {pers.zamedlenie()}, {pers.ogneni_shar()}')

else:
    print('Вы ввели не верную расу')
try:
    slov = pers.__dict__

    with open('../test333.json', 'w', encoding='utf-8') as fl:  # открываем файл в режиме записи
        json.dump(slov, fl, indent=4, ensure_ascii=False)  # сохраняев файл в формат json

except NameError:
    pass
