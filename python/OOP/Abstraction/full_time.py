#
from Employee import Employee


class full_time(Employee):
    def __init__(self, nm, sal):
        super().__init__(nm, sal)

    def showdetails(self):
        return super().showdetails()


v1 = full_time("ketna", 10000)
print(v1.showdetails())
