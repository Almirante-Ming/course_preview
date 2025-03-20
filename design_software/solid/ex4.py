from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        return f"Processed {amount} using Credit Card {self.card_number}"

class PixProcessor(PaymentProcessor):
    def __init__(self, key):
        self.key = key

    def process_payment(self, amount):
        return f"Processed {amount} using PIX {self.key}"

# ----------------------------------------------------------------------
payment_methods = [
    CreditCardProcessor("1234-5678-9012-3456"),
    PixProcessor("key-pix-123")
]

for method in payment_methods:
    print(method.process_payment(100))