class dog:
    def __init__(self,Type,name):
        self.Type = Type
        self.name = name

    def fun(self):
        print('im a ',self.Type)
        print('im a ',self.name)

bobber = dog('mammal','lab')
bobber.fun()