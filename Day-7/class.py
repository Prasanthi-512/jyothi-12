class Movie:
    hero=""
    title=""
    budget=0
    def display(self, hero,title,budget):
        print(f"hero is {hero} and the title is {title} and the budget is {budget}cr")
x=Movie()
x.hero="Pawan kalyan"
print(x.hero)
x.title="Kushi"
print(x.title)
x.budget=40000
print(x.budget)
x.display("Ram Charan","Orange",400)



# class Student:
#     Name =  "Prasanthi"
#     Rollno = 12
# x = Student()
# print(x.Name)
# print(x.Rollno)


# class Student:
#     def display(self):
#         print("Prasanthi....")
# x=Student
# x.display("Prasanthi") 



# class  modify:
#     def __init__(self,name):
#         self.name=name 
#     def changename(self,n):
#         self.name=n
#     def newname(self):
#         print(f"New name is {self.name}")
# a=modify("sai")
# a.changename('Jyothi')
# a.newname()


# class user:
#     def __init__(self):
#         self.name=input()
#     def change(self):
#         self.name=input()
#     def new(self):
#         print(f"New name is {self.name}")
# a=user()
# a.change()
# a.new()



# class Car:
#     wheels = 4
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
# c=Car("BMW","Toyato")
# print("The brand of the car is ",c.brand,"Model is ",c.model,"wheels ",c.wheels)




