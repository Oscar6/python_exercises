# class MyClass:
#     def Greeting():
#         print("hello world")

# digitalCrafts = MyClass.Greeting() # . operator allows for Greeting to be called

# ////////////// # //////////////

# class Friend:
#     def Greeting(species):
#         print("hello " + species)

# Oscar = Friend.Greeting("Oscar")
# Olive = Friend.Greeting("Olive")

# ////////////// # //////////////

# class Friend:
#     def __init__(self, firstN, lastN):
#         self.firstName = firstN,
#         self.lastName = lastN

#     def GreetingFriend(self):
#         print(f"Hello {self.firstName} {self.lastName}")

#     def Greeting(self, species):
#         print("hello " + species)

# Oscar = Friend("Oscar", "Miranda")
# Oscar.GreetingFriend()
# Oscar.firstName = "Osc"
# Oscar.GreetingFriend()

# Olive = Friend("Olive", "Dogter")
# Olive.GreetingFriend()

# ////////////// # //////////////
class Car:
    greeting = "Hello world"                # class variable applicable to all objects
    def __init__(self, make, model, color): # method
        self.make = make
        self.model = model                  #instance variables
        self.color = color

    def ChangeColor(self, toColor):         # method
        print(f"Changing from {self.color} to {toColor}")
        self.color = toColor
        print(f"New color is {self.color}")

    def openDoor(self):
        print("open door")

    def displayColor(self):
        print(f"The color of the car is {self.color}")
        return self.color

    @classmethod
    def instanceMethod(cls):
        print(f"this is an instance")

    def instanceMethod1(self):
        print(f"this is an instance {self.color} ")

class ElectricCar(Car):
    def __init__(self, make, model, range, autopilot):
        super().__init__(make, model, "black")
        self.range = range
        self.autopilot = autopilot

    def batteryLife(self, life):
        print(f"battery life is: {life}")

class Hybrid(Car):
    def __init__(self, make, model, color, batteryLife):
        super().__init__(make, model, color)
        self.batteryLife = batteryLife

myHybrid = Hybrid("Toyota", "Prius", "Silver", "2 hours")

myHybrid.ChangeColor("Lime")


# car = Car("Subaru", "Impreza", "Black")     #object
# car.instanceMethod()

# car2 = Car("DMC", "DeLorean", "Silver")
# car.instanceMethod1()


# tesla = ElectricCar("Tesla", "Model 3", "4 hours", "yes")

# print(tesla.displayColor())

# tesla.batteryLife("3 hours")


# car.ChangeColor("Blue")
# print(car.greeting)

# car.openDoor()
# car.displayColor()


# print(car2.greeting)

