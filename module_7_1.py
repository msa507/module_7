class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self. weight = weight
        self.category = category

    def __str__(self):
        str_prod = f'{self.name}, {self.weight}, {self.category}'
        return str_prod


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, 'r')
        get_products = file.read()
        file.close()
        return get_products

    def add(self, *products):
        file_list = self.get_products()
        for name_veg in products:
            if name_veg.name in file_list:
                print(f'Продукт {name_veg.name} уже есть в магазине ')
            else:
                with open(self.__file_name, 'w') as file:
                    file_list = file_list + f'{name_veg}\n'
                    file.write(file_list)
                    file.close()


s1 = Shop()
p1 = Product('Potato', 50.0, 'Vagetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato1', 5.5, 'Vegetables')
p4 = Product('Cocos', 2.4, 'Nuts')

print(p2)

s1.add(p1, p2, p3, p4)

print(s1.get_products())
