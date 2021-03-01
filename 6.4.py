class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


Lambo = SportCar(100, 'White', 'Lambo', False)
Kia = TownCar(30, 'Green', 'Kia', False)
Camry = WorkCar(70, 'Black', 'Camry', True)
Chevrolet = PoliceCar(110, 'Blue',  'Chevrolet', True)
print(Camry.turn_left())
print(f'When {Kia.turn_right()}, then {Lambo.stop()}')
print(f'{Camry.go()} with speed exactly {Camry.show_speed()}')
print(f'{Camry.name} is {Camry.color}')
print(f'Is {Lambo.name} a police car? {Lambo.is_police}')
print(f'Is {Camry.name}  a police car? {Camry.is_police}')
print(Lambo.show_speed())
print(Kia.show_speed())
print(Chevrolet.police())
print(Chevrolet.show_speed())
