<<<<<<< HEAD
# OOPs -> Also called as Object Oriented Programming --- is a way of organizing code that uses objects and classes to represent real-world entities and their behavior.
#  Object has attributes thing that has specific data and can perform certain actions using methods.

# Class is a blueprint for creating objects. It defines the attributes and methods that the objects of that class will have.
# Object is an instance of a class. It is created using the class constructor and can access the attributes and methods defined in the class.
# Encapsulation is the process of hiding the internal details of an object and exposing only the necessary information to the outside world.
# Inheritance is the process of creating a new class that inherits the attributes and methods of an existing class.
# Polymorphism is the ability of an object to take on many forms. It allows objects of different classes to be treated as objects of a common superclass.
# Abstraction is the process of simplifying complex systems by breaking them down into smaller, more manageable parts.
# ---> It allows us to focus on the essential features of an object while ignoring the irrelevant details.

class Dog:
    # Class Attribute -> which is define directly in the class not under any method 
    species = "Canine"
    # Actually in python the constructor is defined using the __init__ method which is used to initialize the attributes of the class
    # __init__ → constructor (initializes the object) ,__del__ → destructor, __str__ → string representation (str(obj)), __len__ → length (len(obj))
    def __init__(self,name,age): # Constructor -> is a special method that is called when an object is created
        self.name = name # Instance Attribute -> which is define under a method using self keyword not in the class directly
        self.age = age
    def bark(self):
        return f"{self.name} is barking"
Dog1 = Dog("Muffin",3) # while creating objects in python we don't use the "new" keyword like in java or c++
Dog2 = Dog("Charlie",5)
print(f"{Dog1.name} is {Dog1.age} years old and belongs to the species {Dog.species}")
print(f"{Dog2.name} is {Dog2.age} years old and belongs to the species {Dog.species}")
print(Dog.species) # accessing the class attribute using the class name directly  we can use the object name also
print(Dog1.bark()) # accessing the method using the object name

print(Dog.species) # Local/CLASS variable -> which is defined in the class directly
print(Dog1.name) # INSTANCE variable -> which is defined under a method using self keyword
print(Dog2.name) # # INSTANCE variable -> which is defined under a method using self keyword

Dog1.name = "kallu"
print(Dog1.name) # updating the instance variable using the object name
Dog2.species = "Labrador"
print(Dog2.species) # updating the class variable using the class name the value of species is changed only for Dog2 object not for Dog1 object
print(Dog1.species) # accessing the class variable using the class name


# Python Inheritance support all types of inheritance like single, multiple, multilevel, hierarchical and hybrid inheritance
# Single Inheritance- -> A child class inherits from a single parent class.
class Animal:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print(f"The name of the dog is {self.name}")
class Labrador(Animal): # Child class inherits from the parent class
    def sound(self):
        print(f"{self.name} barks")

# Multilevel Inheritance ->A child class inherits from a parent class, which in turn inherits from another class.
class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name} guides the blind person way !!!")

# Multiple Inheritance -> A child class inherits from more than one parent class.
class Friendly:
    def greet(self):
        print("The dog is friendly")
class Bulldog(Animal,Friendly):
    def sound(self):
        print(f"{self.name} barks")

lab = Labrador("Charlie")
lab.display_name()
lab.sound()
# lab.guide() # this will give an error because the guide method is not defined in the Labrador class

guideDog = GuideDog("Muffin")
guideDog.display_name()
guideDog.guide()
guideDog.sound()
# guideDog.greet() # this will give an error because the greet method is not defined in the GuideDog class

bullDog = Bulldog("Max") # It can access all the methods
bullDog.display_name()
bullDog.greet()
bullDog.sound()

# Polymorphism -> allows to have same method name but different functionality based on the Object's Context 
# Polymorphism can be achieved through method overriding and method overloading also called compile time polymorphism
# Method Overriding -> when a child class has a method with the same name as a method in the parent class
# Method Overloading -> when a class has multiple methods with the same name but with different parameters
class Cat:
        def sound(self):
            print("Cat Meows") # Default implementation 
# Run time polymorphism: Method Overriding
class Lion(Cat):
        def sound(self):
            print("Lion Roars") # Overriding the method of the parent class
class Beagle(Cat):
        def sound(self):
            print("Beagle Barks") # Overriding the method of the parent class
# Compile-Time Polymorphism: Method Overloading 
# (not natively supported in Python but can be achieved using default arguments or *args and **kwargs)
class Calculator:
    def add(self,a=0,b=0,c=0): # default argument
        x=0
        if a !=None and b != None and c != None:
             x = a+b+c
        elif a !=None and b != None and c == None:
             x = a+b
        return x
cats = [Cat(),Lion(),Beagle()] # list of objects of different classes
for cat in cats:
    cat.sound() # calling the same method on different objects since each object has its own implementation of the sound method
calc = Calculator()
print(calc.add(2,3)) # calling add() with 2 arguments
print(calc.add(2,3,4)) # calling add() with 3 arguments
print(calc.add(1)) # calling add() with no arguments it will use the default values to return the sum 

# Dynamic Binding  is actually related to polymorphism and is the process of resolving method calls at runtime rather than compile time.
# In Python, all method calls are dynamically bound, meaning that the method to be called is determined at runtime based on the type of the object.
# Monkey Patching is a technique used to modify or extend the behavior of a class or module at runtime without changing its source code.
# Monkey patching overrides or injects behavior into existing classes/objects dynamically at runtime.
# Monkey Patching does't actually support the method overridden in the child class it only modifies the method of the object
monkey_patch = Cat()
def new_sound(self):
    print("Cat Purrs") # new implementation 
monkey_patch.sound = new_sound.__get__(monkey_patch) # binding the new method to the object
monkey_patch.sound() # calling the new method

# Abstraction -> it means hiding the complex implementation details and showing only the essential features of the object.
# In python Abstraction can be achieved using Abstract Base Classes (ABC) module which provides the infrastructure for defining abstract base classes.
# Python has two types of abstraction: Data Abstraction and Process Abstraction
# Data Abstraction -> Hiding the internal details of the data and showing only the essential features.
# Process Abstraction -> Hiding the internal details of the process and showing only the essential features.
# Python, we cannot create (instantiate) an object of an abstract class. It actually provides a blueprint for other classes.
from abc import ABC, abstractmethod
class Demo(ABC):
     @abstractmethod
     def method1(self):
        print("This is an abstract method")
        return 
     def method2(self):
        print("This is a concrete method")
class ConcreteDemo(Demo):
     def method1(self): # implementing the abstract method
        # super() keyword is used to call the parent class method
        super().method1() # calling the abstract method from the parent class
        return
# obj = Demo() # This will give an error because we cannot instantiate an abstract class
obj = ConcreteDemo() # creating an object of the concrete class
obj.method1() # calling the implemented abstract method
obj.method2() # calling the concrete method

from abc import ABC, abstractmethod
class Animal(ABC): # Abstract class
    def __init__(self,name): # Constructor for the abstract class
        self.name = name
    @abstractmethod
    def sound(self):
        pass # abstract method
    def display_name(self):  # Concrete method
        print(f"The name of the animal is {self.name}")
# Partial Abstraction -> when a class has both abstract and concrete methods
class Breed(Animal): # Concrete class inheriting from the abstract class
    def sound(self): # implementing the abstract method
        print(f"{self.name} lives in the wild and roars")
class Birds(Animal): # Concrete class inheriting from the abstract class
    def sound(self): # implementing the abstract method
        print(f"{self.name} flies and chirps high in the sky")
animals = [Breed("Lion"),Birds("Eagle")] # list of objects of different classes
for animal in animals:
    animal.display_name() # calling the concrete method
    animal.sound() # calling the implemented abstract method  

# Encapsulation -> is the process of wrapping data and methods into a single unit called class.
# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
# Types of Encapsulation includes public, protected and private
# In Python no true access modifiers (public, private, protected) for classes, methods, or variables.Instead, naming conventions are used — and they apply to variables, methods, and sometimes classes.
# For using these modifiers in class python don't have private or protected but uses INTERNAL class instead
# Public Members-> Accessible from anywhere.
# Protected Members-> Accessible within the class and its subclasses
# Private Members-> Accessible only within the class.
class Car:
    def __init__(self,make,model,year):
        self.__a = 10 # private member
        self.make = make # public member
        self._model = model # protected member
        self.__year = year # private member
    def display_info(self): # public method
        print(f"Car Make: {self.make}, Model: {self._model}, Year: {self.__year}, Price: {self.__price}")
    # Getter and Setter for private member
    def get_year(self): # getter method
        return self.__year
    def set_year(self,year): # setter method
        if year > 1990: # checking the validity of the year
            self.__year = year
        else:  
            print("Invalid Year")
cars = Car("Toyota","Camry",2020)
print(cars.make) # accessing public member
print(cars._model) # accessing protected member (not recommended)
print(cars.get_year()) # accessing private member (will give an error) but we can use th getter method to access it
cars.set_year(2018) # using the setter method to set the value of the private member
print(cars.get_year()) # using the getter method to get the value of the private member

class Demo:
    def __init__(self):
        self.x = 1       # public
        self._y = 2      # protected (by convention)
        self.__z = 3     # private (name mangled)
obj = Demo()
print(obj.x)  # Accessible
print(obj._y) # Accessible but not recommended   
print(obj._Demo__z) # Accessing private member using name mangling  here _Demo is the class name that is prefixed to the private member __z
# print(obj.__z) # This will give an error because __z is a private member

# Interface is actually not in python but we can achieve it using Abstract Base Classes (ABC) module
# Interface in python are of two types formal and informal
# Formal Interface -> is defined using Abstract Base Classes (ABC) module
# Informal Interface -> is defined using regular classes
from abc import ABC, abstractmethod
# Formal Interface 
class demoInterface(ABC): # creating an interface using ABC module
   @abstractmethod
   def method1(self):
      print ("Abstract method1")
      return

   @abstractmethod
   def method2(self):
      print ("Abstract method2")
      return
class DemoClass(demoInterface): # implementing the interface
   def method1(self):
       super().method1() # calling the abstract method from the parent class
   def method2(self):
       super().method2()
obj = DemoClass() # creating an object of the class
obj.method1() # calling the implemented method
obj.method2() # calling the implemented method

# Informal Interface
class practiceInterface: # creating an informal interface using regular class
    def displayMsg(self):
        pass
class newClass(practiceInterface): # implementing the informal interface
    def displayMsg(self):
        print("Implemented method1")
obj.displayMsg() # calling the implemented method
obj = newClass() # creating an object of the class

# Inner Classes  also called nested classes -> If the inner class is instantiated, the object of inner class can also be used by the parent class
# Inner Classes helps to create the group of classes ->  main advantages  it helps to understand the which classes are related
# Inner Classes are of two types -> Multiple Inner Classes,multilevel Inner classes
class student:
    def __init__(self,name):
        self.name = name
        self.subs = self.subjects()
    def show(self):
        print("Name:",self.name)
        self.subs.display()
    class subjects:
        def __init__(self):
            self.sub1 = "Physics"
            self.sub2 = "Chemistry"
            return
        def display(self):
            print("Subjects:",self.sub1, self.sub2)
s1 = student("Ankit")
s1.show()

=======
# OOPs -> Also called as Object Oriented Programming --- is a way of organizing code that uses objects and classes to represent real-world entities and their behavior.
#  Object has attributes thing that has specific data and can perform certain actions using methods.

# Class is a blueprint for creating objects. It defines the attributes and methods that the objects of that class will have.
# Object is an instance of a class. It is created using the class constructor and can access the attributes and methods defined in the class.
# Encapsulation is the process of hiding the internal details of an object and exposing only the necessary information to the outside world.
# Inheritance is the process of creating a new class that inherits the attributes and methods of an existing class.
# Polymorphism is the ability of an object to take on many forms. It allows objects of different classes to be treated as objects of a common superclass.
# Abstraction is the process of simplifying complex systems by breaking them down into smaller, more manageable parts.
# ---> It allows us to focus on the essential features of an object while ignoring the irrelevant details.

class Dog:
    # Class Attribute -> which is define directly in the class not under any method 
    species = "Canine"
    # Actually in python the constructor is defined using the __init__ method which is used to initialize the attributes of the class
    # __init__ → constructor (initializes the object) ,__del__ → destructor, __str__ → string representation (str(obj)), __len__ → length (len(obj))
    def __init__(self,name,age): # Constructor -> is a special method that is called when an object is created
        self.name = name # Instance Attribute -> which is define under a method using self keyword not in the class directly
        self.age = age
    def bark(self):
        return f"{self.name} is barking"
Dog1 = Dog("Muffin",3) # while creating objects in python we don't use the "new" keyword like in java or c++
Dog2 = Dog("Charlie",5)
print(f"{Dog1.name} is {Dog1.age} years old and belongs to the species {Dog.species}")
print(f"{Dog2.name} is {Dog2.age} years old and belongs to the species {Dog.species}")
print(Dog.species) # accessing the class attribute using the class name directly  we can use the object name also
print(Dog1.bark()) # accessing the method using the object name

print(Dog.species) # Local/CLASS variable -> which is defined in the class directly
print(Dog1.name) # INSTANCE variable -> which is defined under a method using self keyword
print(Dog2.name) # # INSTANCE variable -> which is defined under a method using self keyword

Dog1.name = "kallu"
print(Dog1.name) # updating the instance variable using the object name
Dog2.species = "Labrador"
print(Dog2.species) # updating the class variable using the class name the value of species is changed only for Dog2 object not for Dog1 object
print(Dog1.species) # accessing the class variable using the class name


# Python Inheritance support all types of inheritance like single, multiple, multilevel, hierarchical and hybrid inheritance
# Single Inheritance- -> A child class inherits from a single parent class.
class Animal:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print(f"The name of the dog is {self.name}")
class Labrador(Animal): # Child class inherits from the parent class
    def sound(self):
        print(f"{self.name} barks")

# Multilevel Inheritance ->A child class inherits from a parent class, which in turn inherits from another class.
class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name} guides the blind person way !!!")

# Multiple Inheritance -> A child class inherits from more than one parent class.
class Friendly:
    def greet(self):
        print("The dog is friendly")
class Bulldog(Animal,Friendly):
    def sound(self):
        print(f"{self.name} barks")

lab = Labrador("Charlie")
lab.display_name()
lab.sound()
# lab.guide() # this will give an error because the guide method is not defined in the Labrador class

guideDog = GuideDog("Muffin")
guideDog.display_name()
guideDog.guide()
guideDog.sound()
# guideDog.greet() # this will give an error because the greet method is not defined in the GuideDog class

bullDog = Bulldog("Max") # It can access all the methods
bullDog.display_name()
bullDog.greet()
bullDog.sound()

# Polymorphism -> allows to have same method name but different functionality based on the Object's Context 
# Polymorphism can be achieved through method overriding and method overloading also called compile time polymorphism
# Method Overriding -> when a child class has a method with the same name as a method in the parent class
# Method Overloading -> when a class has multiple methods with the same name but with different parameters
class Cat:
        def sound(self):
            print("Cat Meows") # Default implementation 
# Run time polymorphism: Method Overriding
class Lion(Cat):
        def sound(self):
            print("Lion Roars") # Overriding the method of the parent class
class Beagle(Cat):
        def sound(self):
            print("Beagle Barks") # Overriding the method of the parent class
# Compile-Time Polymorphism: Method Overloading 
# (not natively supported in Python but can be achieved using default arguments or *args and **kwargs)
class Calculator:
    def add(self,a=0,b=0,c=0): # default argument
        x=0
        if a !=None and b != None and c != None:
             x = a+b+c
        elif a !=None and b != None and c == None:
             x = a+b
        return x
cats = [Cat(),Lion(),Beagle()] # list of objects of different classes
for cat in cats:
    cat.sound() # calling the same method on different objects since each object has its own implementation of the sound method
calc = Calculator()
print(calc.add(2,3)) # calling add() with 2 arguments
print(calc.add(2,3,4)) # calling add() with 3 arguments
print(calc.add(1)) # calling add() with no arguments it will use the default values to return the sum 

# Dynamic Binding  is actually related to polymorphism and is the process of resolving method calls at runtime rather than compile time.
# In Python, all method calls are dynamically bound, meaning that the method to be called is determined at runtime based on the type of the object.
# Monkey Patching is a technique used to modify or extend the behavior of a class or module at runtime without changing its source code.
# Monkey patching overrides or injects behavior into existing classes/objects dynamically at runtime.
# Monkey Patching does't actually support the method overridden in the child class it only modifies the method of the object
monkey_patch = Cat()
def new_sound(self):
    print("Cat Purrs") # new implementation 
monkey_patch.sound = new_sound.__get__(monkey_patch) # binding the new method to the object
monkey_patch.sound() # calling the new method

# Abstraction -> it means hiding the complex implementation details and showing only the essential features of the object.
# In python Abstraction can be achieved using Abstract Base Classes (ABC) module which provides the infrastructure for defining abstract base classes.
# Python has two types of abstraction: Data Abstraction and Process Abstraction
# Data Abstraction -> Hiding the internal details of the data and showing only the essential features.
# Process Abstraction -> Hiding the internal details of the process and showing only the essential features.
# Python, we cannot create (instantiate) an object of an abstract class. It actually provides a blueprint for other classes.
from abc import ABC, abstractmethod
class Demo(ABC):
     @abstractmethod
     def method1(self):
        print("This is an abstract method")
        return 
     def method2(self):
        print("This is a concrete method")
class ConcreteDemo(Demo):
     def method1(self): # implementing the abstract method
        # super() keyword is used to call the parent class method
        super().method1() # calling the abstract method from the parent class
        return
# obj = Demo() # This will give an error because we cannot instantiate an abstract class
obj = ConcreteDemo() # creating an object of the concrete class
obj.method1() # calling the implemented abstract method
obj.method2() # calling the concrete method

from abc import ABC, abstractmethod
class Animal(ABC): # Abstract class
    def __init__(self,name): # Constructor for the abstract class
        self.name = name
    @abstractmethod
    def sound(self):
        pass # abstract method
    def display_name(self):  # Concrete method
        print(f"The name of the animal is {self.name}")
# Partial Abstraction -> when a class has both abstract and concrete methods
class Breed(Animal): # Concrete class inheriting from the abstract class
    def sound(self): # implementing the abstract method
        print(f"{self.name} lives in the wild and roars")
class Birds(Animal): # Concrete class inheriting from the abstract class
    def sound(self): # implementing the abstract method
        print(f"{self.name} flies and chirps high in the sky")
animals = [Breed("Lion"),Birds("Eagle")] # list of objects of different classes
for animal in animals:
    animal.display_name() # calling the concrete method
    animal.sound() # calling the implemented abstract method  

# Encapsulation -> is the process of wrapping data and methods into a single unit called class.
# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
# Types of Encapsulation includes public, protected and private
# In Python no true access modifiers (public, private, protected) for classes, methods, or variables.Instead, naming conventions are used — and they apply to variables, methods, and sometimes classes.
# For using these modifiers in class python don't have private or protected but uses INTERNAL class instead
# Public Members-> Accessible from anywhere.
# Protected Members-> Accessible within the class and its subclasses
# Private Members-> Accessible only within the class.
class Car:
    def __init__(self,make,model,year):
        self.__a = 10 # private member
        self.make = make # public member
        self._model = model # protected member
        self.__year = year # private member
    def display_info(self): # public method
        print(f"Car Make: {self.make}, Model: {self._model}, Year: {self.__year}, Price: {self.__price}")
    # Getter and Setter for private member
    def get_year(self): # getter method
        return self.__year
    def set_year(self,year): # setter method
        if year > 1990: # checking the validity of the year
            self.__year = year
        else:  
            print("Invalid Year")
cars = Car("Toyota","Camry",2020)
print(cars.make) # accessing public member
print(cars._model) # accessing protected member (not recommended)
print(cars.get_year()) # accessing private member (will give an error) but we can use th getter method to access it
cars.set_year(2018) # using the setter method to set the value of the private member
print(cars.get_year()) # using the getter method to get the value of the private member

class Demo:
    def __init__(self):
        self.x = 1       # public
        self._y = 2      # protected (by convention)
        self.__z = 3     # private (name mangled)
obj = Demo()
print(obj.x)  # Accessible
print(obj._y) # Accessible but not recommended   
print(obj._Demo__z) # Accessing private member using name mangling  here _Demo is the class name that is prefixed to the private member __z
# print(obj.__z) # This will give an error because __z is a private member

# Interface is actually not in python but we can achieve it using Abstract Base Classes (ABC) module
# Interface in python are of two types formal and informal
# Formal Interface -> is defined using Abstract Base Classes (ABC) module
# Informal Interface -> is defined using regular classes
from abc import ABC, abstractmethod
# Formal Interface 
class demoInterface(ABC): # creating an interface using ABC module
   @abstractmethod
   def method1(self):
      print ("Abstract method1")
      return

   @abstractmethod
   def method2(self):
      print ("Abstract method2")
      return
class DemoClass(demoInterface): # implementing the interface
   def method1(self):
       super().method1() # calling the abstract method from the parent class
   def method2(self):
       super().method2()
obj = DemoClass() # creating an object of the class
obj.method1() # calling the implemented method
obj.method2() # calling the implemented method

# Informal Interface
class practiceInterface: # creating an informal interface using regular class
    def displayMsg(self):
        pass
class newClass(practiceInterface): # implementing the informal interface
    def displayMsg(self):
        print("Implemented method1")
obj.displayMsg() # calling the implemented method
obj = newClass() # creating an object of the class

# Inner Classes  also called nested classes -> If the inner class is instantiated, the object of inner class can also be used by the parent class
# Inner Classes helps to create the group of classes ->  main advantages  it helps to understand the which classes are related
# Inner Classes are of two types -> Multiple Inner Classes,multilevel Inner classes
class student:
    def __init__(self,name):
        self.name = name
        self.subs = self.subjects()
    def show(self):
        print("Name:",self.name)
        self.subs.display()
    class subjects:
        def __init__(self):
            self.sub1 = "Physics"
            self.sub2 = "Chemistry"
            return
        def display(self):
            print("Subjects:",self.sub1, self.sub2)
s1 = student("Ankit")
s1.show()

>>>>>>> d5a4f36590f1dec64f6b24f7307b0aa4ccb2ff03
