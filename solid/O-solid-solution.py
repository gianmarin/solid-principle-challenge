# Here your solution
from abc import ABC, abstractmethod

class FeeCalculatorInterface:
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def calculate_fee(self):
        pass

class CreditCardPaymentMethod(FeeCalculatorInterface):
    def calculate_fee(self):
        return self.amount * 0.03

class PaypalPaymentMethod(FeeCalculatorInterface):
    def calculate_fee(self):
        return self.amount * 0.05

class BankTransferPaymentMethod(FeeCalculatorInterface):
    def calculate_fee(self):
        return self.amount * 2.5