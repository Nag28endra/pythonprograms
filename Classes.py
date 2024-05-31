# import classes2
#  class Dog():
#      def __init__(self,name,age):
#         self.name = name
#         self.age = age
#      def sit(self):
#         print(self.name.title()+" is now sitting") 
#      def roll(self):
#         print(self.name.title()+" is now rolling")

# obj=Dog("charlie",2)
# print(f'the dog name is {obj.name} and its age is {obj.age}') #accessing the attributes using the instance
# obj.sit()
# obj.roll()

# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def describe_restaurant(self):
#         print("the restaurant "+self.restaurant_name.title()+" cuisine type is "+self.cuisine_type.title())
#     def open_restaurant(self):
#         print("the restaurant "+self.restaurant_name.title()+" is opened")

# restaurant = Restaurant('Spicy','Chinese Cooking')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# class User():
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def describe_user(self):
#         print('First Name '+self.first_name.title())
#         print("Last Name "+self.last_name.title())
#     def greet_user(self):
#         print("heloo "+self.first_name.title()+" "+self.last_name.title())

# user = User('Nagendra',"Marisetti")
# user.describe_user()
# user.greet_user()

# class Car():
#     def __init__(self,model,name,year):
#         self.model = model
#         self.name = name
#         self.year = year
#         self.odometer_reading = 0
#     def car_description(self):
#         print(f'the car name is {self.name} and model is {self.model} and manufactured in the year {self.year}')
#     def odometerReading(self):
#         print(f'the odometer reading of the car is {self.odometer_reading} miles')
# class MyCar(Car):
#     def __init__(self, model, name, year):
#         super().__init__( model, name,year)
# car = MyCar('Au16',"Tesla",'2018')
# car.car_description()
# car.odometer_reading = 22
# car.odometerReading()

# classes2.check_palindrome(121)

# class Dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(f'the dog name is {self.name.title()} and it is sitting')
#     def walking(self):
#         print(f'it is of age {self.age} ')
# object = Dog('max',12)   
# object.sit()
# object.walking()

