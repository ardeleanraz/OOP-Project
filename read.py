def read_departament_id():

    from departament import Departament
    print(Departament.members)
    try:
        id_departament = input('Alegeti id-ul unui departament!:')
        if int(id_departament) in Departament.members:
            return int(id_departament)
    except TypeError:
        return None



def read_employee_id():


    from employee import Employee
    print(Employee.members)
    try:
        angajat_id = input('Alegeti id-ul unui angajat!')
        if int(angajat_id) in Employee.members:
            return int(angajat_id)
    except TypeError:
        return None




def read_product_id():


    from product import Product
    print(Product.items)
    try:
        product_id = input('Alegeti id-ul unui produs:')
        if int(product_id) in Product.items:
            return int(product_id)
    except TypeError:
        return None