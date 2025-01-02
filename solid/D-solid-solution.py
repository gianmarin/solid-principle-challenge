# Here your solution
from abc import ABC, abstractmethod

class PaymentInterface(ABC):
    @abstractmethod
    def pay(self):
        pass

class PaypalPayment(PaymentInterface):
    def pay(self, amount: float):
        print(f"Paying {amount} using PayPal...")

class ManagerPayment:
    def __init__(self, payment_type: PaymentInterface):
        self.payment_type = payment_type

    def process_payment(self, amount: float):
        self.payment_type.pay(amount)
