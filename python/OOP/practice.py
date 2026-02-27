# -------------------------------------------------
# class method -
# when i want to work with class level data -
# first parameter should be cls - refrence variable
# you can only access class level attribute inside class method
# @classmethod - decorator
# object refrence is in the first parameter of the method
# can you access obj level data using class refrence
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
        self.welcome()
        if self.percentage() > 42:
            return "student pass"
        else:
            return "student fail"

    @classmethod  # decorator to define class method to assign class method
    def change_traner(
        cls, trainer_name
    ):  # cls refrence variable used in class method only to access class level data
        cls.welcome()
        cls.trainer = trainer_name

    @classmethod
    def apply_dic(cls, dis):
        dfees = cls.fees * dis / 100
        cls.fees = cls.fees - dfees

    # static method
    @staticmethod
    def welcome():  #
        print("welcome")

    @staticmethod
    def cal_sp_course(fees, dis):  # static method
        dp = fees * dis / 100
        sp = fees - dp
        print(sp)


s1 = Student("om", 17)
# print(s1.welcome())
# print(s1.change_traner("rahul"))
Student.cal_sp_course(30000, 22)

# -------------------------------------------
# static method -
# explain - its' like a function without any refrence variable as a first parameter
# it act as a helper/utility function -
# @staticmethod - decorator
# you can call static method by using object refrence and class
# ex

# -------------------------------------------
# ex - 1 Account


class account:
    bank_name = "sbi"  # CASS ATTRIBUTE - class level attribute
    branch = "pune"
    ifsc_no = "SBIN1234"

    def __init__(self, nm, ac, bal=0):  # constructor

        self.name = nm  # instance attribute object level attribute
        self.account_no = ac
        self.balance = bal

    def details(self):  # instance method
        data = f"""
        Bank       :   {self.bank_name}
        Branch     :   {self.branch}
        IFSC       :   {self.ifsc_no}
        {'-'*20}
        Name       :   {self.name}
        Account No :   {self.account_no}
        Balance    :   {self.balance}
        """
        print(data)

    def check_bal(self):  # instance method
        print(f"your balance is {self.balance}")  # self.balance

    def deposit(self, amount):
        if isinstance(amount, (int, float)):  # to check if amount is int or float
            if amount > 0:
                self.balance = self.balance + amount
                return f"{self.account_no} credited by {amount} and balance is {self.balance}"
            else:
                return f"invalid amount"
        else:
            return "enter numeric value"

    def withdraw(self, get_amount):
        if isinstance(get_amount, (int, float)):
            if get_amount <= self.balance:
                self.balance = self.balance - get_amount
                return f"{self.account_no} debited by {get_amount} and balance is {self.balance}"
            else:
                return f"insufficient balance"
        else:
            return "enter numeric value"

    @staticmethod
    def calculate_ci(principal, rate, years, n=1):
        amount = principal * (1 + (rate / (100 * n))) ** (n * years)
        interest = amount - principal
        return round(interest, 2)

    @staticmethod
    def calculate_emi(p, r, n):
        monthly_r = r / (12 * 100)

        # EMI Formula: [P x R x (1+R)^N]/[(1+R)^N-1]
        emi = (p * monthly_r * (1 + monthly_r) ** n) / ((1 + monthly_r) ** n - 1)
        return round(emi, 2)


# --- Testing the new features ---

# 1. Calculate Compound Interest for 10,000 at 5% for 2 years
ci_val = account.calculate_ci(10000, 5, 2)
print(f"Compound Interest: {ci_val}")

# 2. Calculate EMI for a loan of 5,00,000 at 8.5% for 24 months (2 years)
emi_val = account.calculate_emi(500000, 8.5, 24)
print(f"Monthly EMI: {emi_val}")
acc1 = account("om patil", 123456, 30000)
acc2 = account("vaibhav patil", 123458, 20000)
acc3 = account("rahul patil", 123459, 50000)

print(acc1.deposit(5000))

# print(acc1.details())

# print(acc1.check_bal())

# -------------------------------------------

# timeframe - 1:31:00
