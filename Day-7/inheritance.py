
#single inheritance  
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")



# Multiple inheritance
# class Father:
#     def skill(self):
#         print("Father's skills")

# class Mother:
#     def talent(self):
#         print("Mother's talents")

# class Child(Father, Mother):
#     pass

# Multilevel inheritance
# class Grandparent:
#     def greet(self):
#         print("Hello from grandparent")

# class Parent(Grandparent):
#     def welcome(self):
#         print("Welcome from parent")

# class Child(Parent):
#     def hello(self):
#         print("Hello from child")

# Hierachy inheritance
# class Animal:
#     def sound(self):
#         print("Some sound")

# class Dog(Animal):
#     def bark(self):
#         print("Bark")

# class Cat(Animal):
#     def meow(self):
#         print("Meow")



# Hybrid inheritance
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def display(self):
#         print("B")

# class C:
#     def feature(self):
#         print("C")

# class D(B, C):
#     pass




class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        print("Beep beep!")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")


my_car = Car("Honda", "Civic")
my_car.display_info()  
my_car.honk()          
