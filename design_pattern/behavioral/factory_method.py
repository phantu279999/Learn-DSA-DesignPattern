from __future__ import annotations
from abc import ABC, abstractmethod


class News(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def call_operation(self):
        # Calls the factory method to get the product
        product = self.factory_method()
        # Uses the product's operation method
        return product.operation()


class MagazineNews(News):
    def factory_method(self):
        # Returns a specific product instance
        return MagazineProduct()


class ImageNews(News):
    def factory_method(self):
        # Returns a specific product instance
        return ImagesProduct()


class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


class MagazineProduct(Product):
    def operation(self):
        return "Magazine has content containing images"


class ImagesProduct(Product):
    def operation(self):
        return "Images News has content containing images and text"


def client_code(creator: News):
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.call_operation()}", end="")


if __name__ == '__main__':
    client_code(MagazineNews())
    # You can also test with the other creator
    # client_code(ImageNews())