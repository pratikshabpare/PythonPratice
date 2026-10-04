class Car:
    car_type="Sedan"
    def __init__(self,car_name,engine):
        self.car_name=car_name
        self.engine=engine
car1=Car("HondaCity",250)
print(car1.car_name)
print(car1.engine)