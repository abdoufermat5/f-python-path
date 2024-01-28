from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional


class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.quantity * self.price


class Order(NamedTuple):  # the context
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional["Promotion"] = None

    def total(self) -> Decimal:
        return sum([item.total() for item in self.cart], start=Decimal(0))

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)

        return self.total() - discount

    def __repr__(self):
        return f"Customer {self.customer.name} (Fidelity point: {self.customer.fidelity}) ---> <Order total: {self.total():.2f}  due: {self.due():.2f}>"


class Promotion(ABC):
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        """Return discount as a positive dollar amount"""


class FidelityPromo(Promotion):
    def discount(self, order: Order) -> Decimal:
        rate = Decimal("0.05")
        if order.customer.fidelity >= 1000:
            return order.total() * rate
        return Decimal("0")


class BulkItemPromo(Promotion):
    def discount(self, order: Order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal("0.1")  # 10% de réduc
        return discount


class LargeOrderPromo(Promotion):
    def discount(self, order: Order) -> Decimal:
        nb_distinct = len(set(item.product for item in order.cart))
        if nb_distinct >= 10:
            return order.total() * Decimal("0.07")
        return Decimal(0)


if __name__ == "__main__":
    joe = Customer("John Doe", 0)
    ann = Customer("Ann Smith", 1100)
    cart = [
        LineItem("banana", 4, Decimal("0.5")),
        LineItem("apple", 10, Decimal("1.5")),
        LineItem("watermellon", 5, Decimal(5.0)),
    ]

    print(Order(joe, cart, FidelityPromo()))
    print(Order(ann, cart, FidelityPromo()))

    banana_cart = [
        LineItem("banana", 30, Decimal("0.5")),
        LineItem("apple", 10, Decimal("1.5")),
    ]
    print(Order(joe, banana_cart, BulkItemPromo()))

    long_order = [
        LineItem(str(item_code), 1, Decimal(1.0))
        for item_code in range(20)
    ]
    print(Order(joe, long_order, LargeOrderPromo()))
    print(Order(joe, cart, LargeOrderPromo()))
