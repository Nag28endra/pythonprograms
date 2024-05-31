class Car():
    def __init__(self,name,model):
        self.name = name
        self.model = model
    def giveDespc(self):
        print(f'the car name is {self.name} and the model is {self.model}')

    def milage(self):
        print(f'{self.name} gives a milage of 65')
    
class ElectricCar(Car):
    def __init__(self, name, model):
        super().__init__(name, model)

object = ElectricCar("Hyundai", "Creta")
object.giveDespc()
object.milage()
    
