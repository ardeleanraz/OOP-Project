class Employee:
    """Represents any departament member. """

    def __init__(self, name, telephone_number, departament_id):
        """
        :param str name: The name of the employee
        :param str telephone_number: The telephone number of an employee
        :param int departament_id: the ID of the department that this employee works in
        """
        self.name = name
        self.telephone_number = telephone_number
        self.departament_id = departament_id


class Departament:
    """ Represents any departament."""

    def __init__(self, name, manager_id):
        """
        :param str name:  name of the department
        :param int manager_id: the ID of an employee, which is the manager of this department
        """
        self.name = name
        self.manager_id = manager_id

def create_users():
    n = 1
    name = input('Numele angajatului este:')
    telephone_number = input('Numarul de telefon al angajatului este:')
    departament_id = input('ID-ul departamentului este:')
    employee = Employee(name, telephone_number, int(departament_id))
    angajati[n] = employee
    n = n + 1

def create_departament():
    m = 1
    name = input('Numele departamentului este:')
    for employee_id, employee in angajati.items():
        print(employee_id, ':', 'name:', employee.name, ',', 'telephone_number:', employee.telephone_number, ',',
              'ID:', employee.departament_id)
    manager_id = input('Alegeti id-ul un angajat pe care doriti sa il puneti in functia de manager:')

    departament = Departament(name, int(manager_id))
    departamente[m] = departament
    m = m + 1

def print_users():
    for employee_id, employee in angajati.items():
        print(employee_id, ':', 'name:', employee.name, ',', 'telephone_number:', employee.telephone_number, ',',
              'departament_ID:', employee.departament_id)

def print_departament():
    for departament_id, departament in departamente.items():
        print(departament_id, ':', 'departament_name:', departament.name, ',', 'Departament_manager:',
              departament.manager_id)

def print_users_by_dep_id():
    for departament_id, departament in departamente.items():
        print(departament_id, ':', 'departament_name:', departament.name, ',', 'Departament_manager:',
              departament.manager_id)
    id_departament = input('Alegeti id-ul unui departament!:')

    for employee_id, employee in angajati.items():
        if id_departament == str(employee.departament_id):
            print(employee.name)

def change_dep_manager():
    for employee_id, employee in angajati.items():
        print(employee_id, ':', 'name:', employee.name, ',', 'telephone_number:', employee.telephone_number, ',',
              'departament_id:', employee.departament_id)
    employee_id = input('Alegeti id-ul angajatului pe care doriti sa il puneti in functia de manager!:')

    for departament_id, departament in departamente.items():
        print(departament_id, ':', 'departament_name:', departament.name, ',', 'Departament_manager:',
              departament.manager_id)
        id_manager = input('Alegeti id-ul departamentului unde se va face schimbarea!:')
        if id_manager in str(departament_id):
            departament.manager_id = employee_id

def numbers_of_dep_users():
    o = 0
    for departament_id, departament in departamente.items():
        print(departament_id, ':', 'departament_name:', departament.name, ',', 'Departament_manager:',
              departament.manager_id)
    id_departament = input('Alegeti id-ul departamentului pentru care doriti sa vedeti numarul de angajati !:')

    for employee_id, employee in angajati.items():
        if id_departament == str(employee.departament_id):
            o += 1
    print(o)
    o = 0

angajati = {}
departamente = {}
begin = None
while begin != 'q':
    if begin == '1':
        create_users()

    if begin == '2':
         create_departament()

    if begin == '3':
         print_users()

    if begin == '4':
        print_departament()

    if begin == '5':
        print_users_by_dep_id()

    if begin == '6':
        change_dep_manager()

    if begin == '7':
        numbers_of_dep_users()


    print('1:Adauga un nou angajat .')
    print('2:Adauga un nou departament.')
    print('3:Lista angajati.')
    print('4:Lista departamente.')
    print('5:Listati angajatii in functie de departamente.')
    print('6:Inlocuiti managerul unui departament cu un alt angajat.')
    print('7:Printati numarul de angajati dintr-un departament!')
    print('Q:Iesire.')
    begin = input('Choose a option!:')
