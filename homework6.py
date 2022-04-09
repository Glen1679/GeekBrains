import time

# 1 задание
class TrafficLight:
    color = ['red', 'yellow', 'green']
    def __running(self):
        print(TrafficLight.color[0])
        time.sleep(7)
        print(TrafficLight.color[1])
        time.sleep(2)
        print(TrafficLight.color[2])
        time.sleep(7)

a = TrafficLight()
a._TrafficLight__running()

# 2 задание
class Road:
    asphalt_amount_list = []
    #total_asphalt_amount = sum(asphalt_amount_list) Не понимаю, почему не могу просуммировать тут
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        Road.asphalt_amount = self._lenght * self._width * 25
        Road.asphalt_amount_list.append(Road.asphalt_amount)

e_95 = Road(120, 60)
m_105 = Road(90, 30)

print(f'Общее количество асфальта на все участки: {sum(Road.asphalt_amount_list)}')

# 3 задание вероятно не совсем правильно понял с income что делать
class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        #self.income = income
        income_dict = {'wage': 10000, 'bonus': 5000}
        self._income = income_dict['wage'] + income_dict['bonus']


worker_1 = Worker('jon', 'black', 'director')
#worker_2 = Worker('sam', 'smith', 'accounter')

print(worker_1._income)

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(self._income)

accounter = Position('sam', 'smith', 'accounter')

accounter.get_full_name()
accounter.get_total_income()

# 4 задание
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановиласть')
    def turn_direction(self, direction):
        print(f'Машина повернула {direction}')
    def show_speed(self):
        print(self.speed)

a = Car(120,'red', 'Nissan', False)
a.show_speed()

a.stop()
a.go()
a.turn_direction('left')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else: print(self.speed)


town_car_1 = TownCar(80,'green', 'opel', False)
town_car_1.show_speed()

class SportCar(Car):
    def go(self): # без единого метода или признака клас выдавал ошибку
        print('Машина поехала')

sport_car_1 = SportCar(150, 'blue', 'mazda', False)

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(self.speed)

work_car_1 = WorkCar(45, 'green', 'caterpiller', False)
work_car_1.show_speed()
work_car_1.stop()

class PoliceCar(Car):
    def go(self): # без единого метода или признака клас выдавал ошибку
        print('Машина поехала')
police_car_1 = PoliceCar(130, 'police_camo', 'ford', True)
print(police_car_1.speed, police_car_1.color)
police_car_1.go()

# 5 задание

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки объекта Ручка')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки объекта Карандаш')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки объекта Маркер')

pen_1 = Pen('erich_krause')
pencil_1 = Pencil('kohinor')
handle_1 = Handle('erich_krause')

pen_1.draw()
pencil_1.draw()
handle_1.draw()