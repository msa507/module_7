from pprint import pprint

class Product():

    def __init__(self, name, weight, category):
        self.name = name
        self. weight = weight
        self.category = category

    def __str__(self):
        str_prod = (f'{self.name}, {self.weight}, {self.category}')
        return str_prod


class Shop():

    __file_name = "products.txt"

    def get_products(self, __file_name):
        file = open(self.__file_name, 'r')
        file.read()
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.0, 'Vagetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p1)
