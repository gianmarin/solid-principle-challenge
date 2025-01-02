# Here your solution
from abc import ABC, abstractmethod

class IPayment(ABC):
    @abstractmethod
    def pay(self, amount:float)-> None:
        pass

class IRefund(ABC):
    @abstractmethod
    def refund(self, amount:float)-> None:
        pass

class PaymentMethod(IPayment, IRefund):
    def __init__(self, balance: float):
        self.balance = balance 

    def pay(self, amount: float):
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        print(f"[PaymentMethod] Paid {amount}. New balance: {self.balance}")

    def refund(self, amount: float):
        self.balance += amount
        print(f"[PaymentMethod] Refunded {amount}. New balance: {self.balance}")     

class NonRefundableGiftCard(IPayment):
    def __init__(self, balance: float):
        self.balance = balance 
    
    def pay(self, amount: float):
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        print(f"[PaymentMethod] Paid {amount}. New balance: {self.balance}")