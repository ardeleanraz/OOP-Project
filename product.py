class Product:
    product_current_idx = 1
    members= {}
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

    @staticmethod
    def create_product():

        from departament import Departament
        if Departament.members:

            from read import read_departament_id
            departament_id = read_departament_id()
            name = input('Numele produsului este:')
            price = input('Pretul produsului este:')
            product = Product(name, price, departament_id)

            Product.members[Product.product_current_idx] = product
            Product.product_current_idx += 1






    def print_product():

        print(Product.members)

    def most_expensive_product():

        product_price = []
        for id_product, product in Product.members.items():
            product_price.append(product.price)
        print(max(product_price))



    def __str__(self):
        return 'Product_name:' + self.name + ',' + 'Price:' +str(self.price) + ',' + 'Departament_id:' +str(self.departament_id)

    def __repr__(self):
        return "{name},{price},{id_departament}".format(name= self.name, price = self.price , id_departament = self.departament_id)
