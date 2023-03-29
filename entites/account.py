from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, id: str, balance: float):
        self.id = id
        self.balance = balance

    @abstractmethod
    def deposit(self, value: float):
        pass

    @abstractmethod
    def withdraw(self, value: float):
        pass
