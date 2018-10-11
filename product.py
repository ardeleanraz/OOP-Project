


class Product:
    product_current_idx = 1
    """Represent any product"""

    def __init__(self, name, price, departament_id):
        """
        :param str name : name of product
        :param str price : price of product
        :param int|None departament_id: the ID of the department
        """

        self.name = name
        self.price = price
        self.departament_id = departament_id

    def __str__(self):
        return self.name + str(self.price) + str(self.departament_id)

    def __repr__(self):
        return "{name},{price},{id_departament}".format(name= self.name, price = self.price , id_departament = self.departament_id)




def create_product():

    from options import departamente
    if departamente:
        from read import read_departament_id
        departament_id = read_departament_id()
        name = input('Numele produsului este:')
        price = input('Pretul produsului este:')

        product = Product(name, price, departament_id)
        from options import produse
        produse[Product.product_current_idx] = product
        Product.product_current_idx += 1




def print_product():
    from options import produse
    print(produse)



def most_expensive_product():
    product_price = []
    from options import produse
    for id_product, product in produse.items():
        product_price.append(product.price)
    print(max(product_price))


