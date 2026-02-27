# today -
# overriding -

# types of overriding  -
# Explain overriding - allows a subclass to provide a specific implementation of A method or attribute that is already defined in it's superclass.  This is a core concept of object-oriented programming, enabling polymorphism and customization of inherited behavior

#    1. method overriding -
# explain method overriding - Method overriding involves defining a method in the child class with the exact same name and the same number of parameters as a method in its parent class. This allows the child class to provide a different implementation of the method

# ex -


class Animal:
    def speak(self):  # this is an method
        print("Animal is speaking")


class Dog(Animal):
    def speak(self):  # i override the speak method
        super().speak()  # calls the parent class method
        print("dog is speaking")


# Animal_instance = Animal()
# dog_instance = Dog()

# dog_instance.speak()

#    2. attribute overriding -
# explain attribute overriding - Attribute overriding is a type of overriding where the child class provides a different implementation of an attribute that is already defined in its parent class . Attributes, including class and instance variables, can also be overridden. This allows the child class to provide a different value for the attribute
# ex -


class Shape:
    # class attribute
    color = "red"

    def display_color(self):
        print(f"Color: {self.color}")


class Square(Shape):
    # Overriding the class attributed
    color = "blue"


shape_instance = Shape()
square_instance = Square()

# shape_instance.display_color()  # Output: Color: red
# square_instance.display_color()  # Output: Color: blue


# examples -
# basic method overriding -


class operation:
    def add(self, a, b):
        return a + b


class sub(operation):
    def add(self, a, b):
        return a - b


# ex 2


class Vehicle:
    def __init__(self, br, yr):
        self.brand = br
        self.year = yr

    def display_info(self):
        return f"""
        Brand   :    {self.brand}
        year    :    {self.year}
               """


class Car(Vehicle):
    def __init__(self, br, yr, doo):
        super().__init__(br, yr)
        self.door = doo

    def display_info(self):  # overriding the display_info method
        return super().display_info()


# p1 = Vehicle("Honda", 2022)
# p2 = Car("Bmw", 2025)

# print(p1.display_info())
# print(p2.display_info())

# ex 3


class Employee:
    def __init__(self, id, sal):
        self.id = id
        self.salary = sal

    def get_info(self):
        return f"""
        
        id   :   {self.id}
        salary   :   {self.salary}

        """


class SalesEmployee(Employee):
    def __init__(self, id, sal, sales):
        super().__init__(id, sal)
        self.sales = sales

    def get_info(self):
        base_info = super().get_info()
        return base_info + f"   sales   :   {self.sales}/n"


v2 = Employee("234", 8000)
v3 = SalesEmployee("123", 39000, 2300)
print(v3.get_info())
print(v2.get_info())
