from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self):
        self.no_of_type=45
    @abstractmethod
    def start(self):
        pass 