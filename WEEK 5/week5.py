# Assignment one
class Smartphone:
    def __init__(self, brand, model, storage, os, ram, megapixel):
        self.brand  = brand
        self.model = model
        self.storage = storage
        self.os = os
        self.ram = ram
        self.megapixel = megapixel

    def take_picture(self):
        print(f"{self.model} is taking a photo with {self.megapixel} MP camera") 

    def make_call(self,number):
        print(f"Calling {number} from {self.model}")

    def show_specs(self):
        print(f"{self.brand} {self.model} | OS: {self.os} Storage: {self.storage} | RAM: {self.ram}")
        


# Subclass 1: AndroidPhone
class AndroidPhone(Smartphone): # Inheritance
    def take_picture(self):
        print(f"{self.model} (Android) snaps a photo with {self.megapixel}MP")

# Subclass 2: IPhone 
class IPhone(Smartphone): # Inheritance
    def take_picture(self):
        print(f"{self.model} (iPhone) takes a high-quality image 📷")

# Testing the code in class Smartphone
# Instantiate the Smartphone class
phone1 = AndroidPhone("Samsung", "Galaxy S25", 128, "Android", 8, 50)
phone2 = IPhone("Iphone", "12 Pro Max", 128, "iphone", 12, 100)

# Call the methods to test them
phone1.show_specs()
phone1.take_picture()
phone1.make_call("+254712345678")

phone2.show_specs()
phone2.take_picture()
phone2.make_call("+23567890")

# Assignment 2
class Animal:
    def move(self):
        print("This animal moves in some way.")

class Horse(Animal):
    def move(self):
        print("Galloping 🐎")

class Bird(Animal):
    def move(self):
        print("Flying 🐦")

class Fish(Animal):
    def move(self):
        print("Swimming 🐠")

class Vehicle:
    def move(self):
        print("This vehicle moves somehow.")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


# Demonstrating Polymorphism
def describe_movement(objects):
    for obj in objects:
        obj.move()

# Creating instances
objects = [
    Horse(),
    Bird(),
    Fish(),
    Plane(),    
]

# Calling the shared method
describe_movement(objects)
