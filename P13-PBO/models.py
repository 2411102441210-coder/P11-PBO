from dataclasses import dataclass

@dataclass
class Product:
    id: str
    name: str
    price: float

@dataclass
class CartItem:
    product: Product
    quantity: int

    @property
    def subtotal(self) -> float:
        return self.product.price * self.quantity