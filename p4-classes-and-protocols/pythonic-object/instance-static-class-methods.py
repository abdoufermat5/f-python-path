class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    @staticmethod
    def create_car(color, mileage):
        return Car(color, mileage)

    @classmethod
    def create_red_car(cls, mileage):
        return cls('red', mileage)

    def make_sound(self):
        print(self.color, self.mileage, 'vroom')


if __name__ == '__main__':
    car = Car('blue', 20000)
    car.make_sound()

    car1 = Car.create_car('blue', 20000)
    car1.make_sound()
    print("car1 from static method is instance of Car", isinstance(car1, Car))

    car2 = Car.create_red_car(20000)
    car2.make_sound()
    print("car2 from class method is instance of Car", isinstance(car2, Car))
