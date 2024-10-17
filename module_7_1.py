from os import close
from webbrowser import open_new
from pprint import pprint
import io


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'


    def get_products(self):
        file = open(self.__file_name,'r')
        return f'{file.read()}'
        file.close()

    def add (self, *products):
        file = open (self.__file_name,'a')
        for product in products:
            if product.name not in self.get_products():
                string=str(product)
                file.write(f'{string}\n')

            else: print (f'Продукт {product} уже есть в магазине')

        file.close()
        pass

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
