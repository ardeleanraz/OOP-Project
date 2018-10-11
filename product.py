def create_product():


    from classe import  Departament
    if Departament.members:
        from read import read_departament_id
        departament_id = read_departament_id()
        name = input('Numele produsului este:')
        price = input('Pretul produsului este:')
        from classe import Product
        product = Product(name, price, departament_id)

        Product.items[Product.product_current_idx] = product
        Product.product_current_idx += 1




def print_product():
    from classe import Product
    print(Product.items)



def most_expensive_product():
    from classe import Product
    product_price = []
    for id_product, product in Product.items.items():
        product_price.append(product.price)
    print(max(product_price))