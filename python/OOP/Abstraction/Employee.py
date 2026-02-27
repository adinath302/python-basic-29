# abstaraction function -

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, nm, sal):
        self.name = nm
        self.salary = sal

    @abstractmethod
    def showdetails(self):
        pass

        # salary calculation
        # show details
