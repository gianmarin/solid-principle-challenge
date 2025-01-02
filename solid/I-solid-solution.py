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

class IHandleDispute(ABC):
    @abstractmethod
    def handle_dispute(self, dispute_id: str) -> None:
        pass

class BasicGiftCard(IPayment):
    def pay(self, amount: float) -> None:
        print(f"Gift card used to pay {amount}.")