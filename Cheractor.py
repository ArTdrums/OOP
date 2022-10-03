class Cheractor:
    def __init__(self, nik, rasa, pol, color_yeas, tip_vneshnosti, zdorovie, basovi_uron):
        self.nik = nik
        self.rasa = rasa
        self.pol = pol
        self.color_yeas = color_yeas
        self.tip_vneshosti = tip_vneshnosti
        self.zdorovie = zdorovie
        self.basovi_uron = basovi_uron

    def info_sup(self):  # создаем метод , который возвращает все свойства
        return print(f'вы выбрали персонажа со след характеристиками: Имя  {self.nik},' \
                     f' расой {self.rasa}, полом {self.pol}, цветом глаз {self.color_yeas}, ' \
                     f'типом внешности {self.tip_vneshosti}, здоровьем {self.zdorovie}, базовым уроном {self.basovi_uron}')

    def ischelenie(self):
        print('исцеление - восстанавливает 5 здоровья')
