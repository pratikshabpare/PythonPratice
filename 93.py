class Vertebrate:
    def __init__(self,name):
        self.name=name
        self.spine=True
    def move(self):
        print(f"{self.name} is moving")
class Mammal(Vertebrate):
    def __init__(self,name,fur_color):
        super().__init__(name)
        self.fur_color=fur_color
    def nusre(self):
        print(f"{self.name} is nusring its young")
        