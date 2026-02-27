# last session :
# class >> attributes
#       >> types

# todays topic :
# class >> methods
#       >> types

# -------------------------------------------
# methods - method is a function which is defined inside a class
# methods are used to perform some operation on data
# method is a function which is defined inside a class it is used to perform some operation on data

# 3 types of method -
#       instance method -
#       class method -
#       static method  -


# -------------------------------------------
# instance method -
# used to perform operation on object level data -
# first parameter should be self
# we can call instance method inside class by using self and outside class by using object refrence variable
# we can access class level data inside instance method by using class name
# ex
class Student:
    institute = "abc"
    course = "data analytics"
    trainer = "keshav"
    fees = 40000

    def __init__(self, nm, ag):  # constructor
        self.name = nm
        self.age = ag
        self.marks = {}

    def details(self):  # instance method
        data = f""" 
            name : {self.name}
            age  : {self.age}
            course: {Student.course} # we can access class level data inside instance method by using class name
            trainer: {Student.trainer}
        """
        print(data)

    # to add marks
    def add_marks(self, sub, marks):
        self.marks[sub] = marks  # to store marks in dict
        return "marks added"

    # to calculate percentage
    def percentage(self):
        obt = 0  # it's an local variable
        for marks in self.marks.values():
            obt = obt + marks
        total = len(self.marks) * 100
        per = (obt / total) * 100
        return per

    # calculate
    def grade(self):  # method
        if self.percentage() > 90:
            return "A+"
        elif self.percentage() > 80:
            return "A"
        elif self.percentage() > 70:
            return "B+"
        elif self.percentage() > 60:
            return "B"
        else:
            return "C"

    def result(self):
        if self.percentage() > 42:
            return "student pass"
        else:
            return "student fail"


# s1 = Student("om", 17)
# s2 = Student("kartik", 27)
# print(s1.details())
# print(s2.details())
# print(s1.add_marks("math", 90))  # to add marks in dict
# print(s1.add_marks("science", 80))  # to add marks in dict
# print(s1.add_marks("economics", 80))  # to add marks in dict
# print(s2.add_marks("science", 90))  # to add marks in dict
# print(s1.marks)  # it has marks
# print(s2.marks)
# print(s1.percentage())
# print(s1.grade())  # to calcu the grades
# print(s1.result())

# -------------------------------------------
# salary id depart company_name operation = "data_print" "House Rent Allowance (hra)" "Dearness Allowance (da)" "pf"


class employee:
    # class attribute - class level data to store
    company = "apple"

    def __init__(self, nm, sal, dep):
        self.name = nm
        self.salary = sal
        self.department = dep

    # show data
    def display(self):  # instance method
        data = f"""
        company   :   {self.company}
        name      :   {self.name}
        salary    :   {self.salary}
        department:   {self.department}
        """
        print(data)

    # House Rent Allowance (hra)
    def hra(self):
        hra = (10 / 100) * self.salary
        return hra

    # Dearness Allowance
    def da(self):
        is_da = (5 / 100) * self.salary
        return is_da

    # pf
    def is_pf(self):
        pf_rate = 0.12
        pf_amount = pf_rate * (self.salary + self.da())
        return pf_amount


# p1 = employee("keshav", 50000, "IT")
# print(p1.hra())
# print(p1.da())
# print(p1.is_pf()) # use "()" to call the method


# -------------------------------------------
# class method -
# when i want to work with class level data -
# first parameter should be cls - refrence variable
# you can only access class level attribute inside class method
# @classmethod - decorator
# ex
class Student:
    institute = "abc"
    course = "data analytics"
    trainer = "keshav"
    fees = 40000

    def __init__(self, nm, ag):  # constructor
        self.name = nm
        self.age = ag
        self.marks = {}

    def details(self):  # instance method
        data = f""" 
            name : {self.name}
            age  : {self.age}
            course: {Student.course} # we can access class level data inside instance method by using class name
            trainer: {Student.trainer}
        """
        print(data)

    # to add marks
    def add_marks(self, sub, marks):
        self.marks[sub] = marks  # to store marks in dict
        return "marks added"

    # to calculate percentage
    def percentage(self):
        obt = 0  # it's an local variable
        for marks in self.marks.values():
            obt = obt + marks
        total = len(self.marks) * 100
        per = (obt / total) * 100
        return per

    # calculate
    def grade(self):  # method
        if self.percentage() > 90:
            return "A+"
        elif self.percentage() > 80:
            return "A"
        elif self.percentage() > 70:
            return "B+"
        elif self.percentage() > 60:
            return "B"
        else:
            return "C"

    def result(self):
        if self.percentage() > 42:
            return "student pass"
        else:
            return "student fail"


# s1 = Student("om", 17)
# s2 = Student("kartik", 27)
# print(s1.details())
# print(s2.details())
# print(s1.add_marks("math", 90))  # to add marks in dict
# print(s1.add_marks("science", 80))  # to add marks in dict
# print(s1.add_marks("economics", 80))  # to add marks in dict
# print(s2.add_marks("science", 90))  # to add marks in dict
# print(s1.marks)  # it has marks
# print(s2.marks)
# print(s1.percentage())
# print(s1.grade())  # to calcu the grades
# print(s1.result())

# -------------------------------------------
# static method -
# -------------------------------------------
# -------------------------------------------
# -------------------------------------------
# -------------------------------------------
# -------------------------------------------
# -------------------------------------------
# -------------------------------------------

# timeframe 1:35:00
