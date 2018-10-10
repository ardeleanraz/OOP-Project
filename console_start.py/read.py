from departament import departamente
from employee import angajati
from product import produse


def read_departament_id():
    print(departamente)
    try:
        id_departament = input('Alegeti id-ul unui departament!:')
        if int(id_departament) in departamente:
            return int(id_departament)
    except TypeError:
        return None



def read_employee_id():
    print(angajati)
    try:
        angajat_id = input('Alegeti id-ul unui angajat!')
        if int(angajat_id) in angajati:
            return int(angajat_id)
    except TypeError:
        return None




def read_product_id():
    print(produse)
    try:
        product_id = input('Alegeti id-ul unui produs:')
        if int(product_id) in produse:
            return int(product_id)
    except TypeError:
        return None