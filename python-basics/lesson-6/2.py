"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    _length = 0
    _width = 0
    _mass = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        self._mass = self._length * self._width * 25 * 5
        print('Target mass of asphalt is', round(self._mass / 1000), 'тонн')


road = Road(5000, 20)
road.calc_mass()

road2 = Road(6000, 10)
road2.calc_mass()