
def read_departament_id():

    from options import departamente
    print(departamente)
    try:
        id_departament = input('Alegeti id-ul unui departament!:')
        if int(id_departament) in departamente:
            return int(id_departament)
    except TypeError:
        return None



def read_employee_id():

    from options import angajati
    print(angajati)
    try:
        angajat_id = input('Alegeti id-ul unui angajat!')
        if int(angajat_id) in angajati:
            return int(angajat_id)
    except TypeError:
        return None




def read_product_id():

    from options import produse
    print(produse)
    try:
        product_id = input('Alegeti id-ul unui produs:')
        if int(product_id) in produse:
            return int(product_id)
    except TypeError:
        return None