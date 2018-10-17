from departament import Departament
from employee import Employee
from product import Product


def read_employee_id():
    print(Employee.members)
    try:
        angajat_id = input('Alegeti id-ul unui angajat!')
        if int(angajat_id) in Employee.members:
            return int(angajat_id)
    except TypeError:
        return None


def read_product_id():
    print(Product.members)
    try:
        product_id = input('Alegeti id-ul unui produs:')
        if int(product_id) in Product.members:
            return int(product_id)
    except TypeError:
        return None



def read_departament_id():
    print(Departament.members)
    try:
        id_departament = input('Alegeti id-ul unui departament!:')
        if int(id_departament) in Departament.members:
            return int(id_departament)
    except TypeError:
        return None