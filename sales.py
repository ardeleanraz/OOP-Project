def create_sale():
    from classe import Product

    if Product.items:
        from read import read_product_id
        product_id = read_product_id()
        year = input('Anul in care s-a fabricat produsul:')
        month = input('Luna in care s-a fabricat produsul:')
        day = input('Ziua in care s-a fabricat produsul:')

        from classe import Employee
        if Employee.members:
            from read import read_employee_id
            employee_id = read_employee_id()
        else:
            employee_id = None

        from classe import Sale
        sale = Sale(product_id, int(year), int(month), int(day), employee_id)
        Sale.items[Sale.sale_current_idx] = sale
        Sale.sale_current_idx += 1


def print_sales():
    from classe import Sale
    print(Sale.items)