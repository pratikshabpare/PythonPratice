from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        result=3.14 * self.radius * self.radius
        print("Area of Circle=",result)
circle=Circle(5)
circle.area()