#Class

print(type([1,2,3]))
print(type((1,2,3)))
print(type(200))
print(type(20.0))
#class defination
class Sample():
   pass

x=Sample()
print(type(x))

class Dog():
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

myDog=Dog(breed='Lab',name="sammy")
print(myDog.breed)
print(myDog.name)

#class method
class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius * Circle.pi

    def set_radius(self,new_r):
        self.radius=new_r

myc = Circle()
print(myc.radius)
myc.set_radius(100)
print(myc.area())

#INHERITANCE
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

mya = Animal()
mya.whoAmI()
mya.eat()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("Dog eating")

myDog = Dog()
myDog.whoAmI()
myDog.eat()
myDog.bark()

#SPACIAL METHODS

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author =author
        self.pages = pages

    def __str__(self):
        return "Title : {}, Author: {}, Pages : {}".format(self.title,self.author,self.pages)
    def __len__(self):
        return self.pages


b = Book("Pythone","Jose",200)
#print(b)
print(len(b))
