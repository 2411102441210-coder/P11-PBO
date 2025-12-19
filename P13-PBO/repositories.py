import logging
from models import Product

LOGGER = logging.getLogger('REPOSITORY')

class ProductRepository:
    def __init__(self):
        self._products = {
            "P001": Product(id="P001", name="Laptop Gaming", price=15000000),
            "P002": Product(id="P002", name="Mouse Wireless", price=250000),
            "P003": Product(id="P003", name="Keyboard Mech", price=800000),
        }
        LOGGER.info("ProductRepository initialized with 3 products.")

    def get_all(self) -> list[Product]:
        return list(self._products.values())

    def get_by_id(self, product_id: str) -> Product | None:
        return self._products.get(product_id)