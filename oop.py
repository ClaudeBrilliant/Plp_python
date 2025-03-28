class vehicles:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self):
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")

#Inheritance
class car(vehicles):
    pass

vehicles = vehicles("lorry", "Red")
vehicles.display()

#Polimorphism
class car:
    def move(self):
        print("Car is driving")

class human:
    def move(self):
        print("Human is walking")

#create an instance of the car,human class
car1 = car()
human1 = human()
#call the move method of the car, human class
car1.move()
human1.move()
#Output

# Using polymorphism to call the same method on different objects
for movement in (car1, human1):
    movement.move()


#Encapsulation
class car:
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')
        print('Software update complete')

redcar = car()
redcar.drive()
#redcar.__updateSoftware()  not accessible from object

# Accessing __updateSoftware using a public method
class car:
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')
        print('Software update complete')

    def updateSoftware(self):
        self.__updateSoftware()

redcar = car()
redcar.drive()
redcar.updateSoftware()  # Accessing private method via public method