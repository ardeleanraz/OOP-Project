class Departament:
    """ Represents any departament."""

    def __init__(self, name, manager_id):
        """
        :param str name:  name of the department
        :param int|None manager_id: the ID of an employee, which is the manager of this department
        """
        self.name = name
        self.manager_id = manager_id

    def __str__(self):
        return self.name + ',' + str(self.manager_id)

    def __repr__(self):
        return "{name}, {manager_id}".format(name=self.name, manager_id=self.manager_id)




m = 1
departamente = {}



def create_departament():
    global m
    name = input('Numele departamentului este:')
    departament = Departament(name, None)
    if angajati:
        manager_id = read_employee_id()
    else:
        manager_id = None
    departament = Departament(name, manager_id)
    departamente[m] = departament
    m = m + 1




def print_departament():
    print(departamente)




def print_departament_product():
    product_dep = []
    print(departamente)
    id_departament = input('Alegete id-ul unui departament pentru care doriti sa vedeti produsele :')

    for product_id , product in produse.items():
        if id_departament in str(product.departament_id):
            product_dep.append(product.price)

    print(product_dep)



def print_users_by_dep_id():
    print(departamente)
    id_departament = input('Alegeti id-ul unui departament!:')

    for employee_id, employee in angajati.items():
        if id_departament == str(employee.departament_id):
            print(employee.name)



def change_dep_manager():
    id_departament = read_departament_id()

    employee_id = read_employee_id()

    departamente[id_departament].manager_id = employee_id




def numbers_of_dep_users():
    o = 0
    print(departamente)
    id_departament = input('Alegeti id-ul departamentului pentru care doriti sa vedeti numarul de angajati !:')

    for employee_id, employee in angajati.items():
        if id_departament == str(employee.departament_id):
            o += 1
    print(o)




def read_departament_id():
    print(departamente)
    try:
        id_departament = input('Alegeti id-ul unui departament!:')
        if int(id_departament) in departamente:
            return int(id_departament)
    except TypeError:
        return None