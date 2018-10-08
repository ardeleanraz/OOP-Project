class Employee:
    """Represents any departament member. """

    def __init__(self, name, telephone_number, departament_id):
        """
        :param str name: The name of the employee
        :param str telephone_number: The telephone number of an employee
        :param int|None department_id: the ID of the department that this employee works in
        """
        self.name = name
        self.telephone_number = telephone_number
        self.departament_id = departament_id

    def __str__(self):
        return self.name + ',' + self.telephone_number + ',' + str(self.departament_id)


    def __repr__(self):
        return "{name} {telephone_number} {departament_id}".format(name = self.name, telephone_number = self.telephone_number ,departament_id = self.departament_id)

class Departament:
    """ Represents any departament."""
    def __init__(self, name, manager_id):
        """
        :param str name:  name of the department
        ::param int|None manager_id: the ID of an employee, which is the manager of this department
        """
        self.name = name
        self.manager_id = manager_id

    def __str__(self):
        return self.name + ',' + self.manager_id

    def __repr__(self):
        return "{name}  {manager_id}".format(name = self.name , manager_id = self.manager_id )

def create_users():
    global n
    name = input('Numele angajatului este:')
    telephone_number = input('Numarul de telefon al angajatului este:')
    employee = Employee(name, telephone_number, None)
    if departamente:
        departament_id = read_departament_id()
    else:
        departament_id = None
    employee = Employee(name , telephone_number , departament_id)
    angajati[n] = employee
    n = n + 1

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



def print_users():
    print(angajati)


def print_departament():
    print(departamente)

def print_users_by_dep_id():
    print(departamente)
    id_departament = input('Alegeti id-ul unui departament!:')

    for employee_id, employee in angajati.items():
        if id_departament == str(employee.departament_id):
            print(employee.name)


def change_dep_manager():
    id_departament = read_departament_id()

    id_angajat = read_employee_id()

    departamente[id_departament].manager_id = id_angajat




def numbers_of_dep_users():
    o = 0
    print(departamente)
    id_departament = input('Alegeti id-ul departamentului pentru care doriti sa vedeti numarul de angajati !:')

    for employee_id, employee in angajati.items():
        if id_departament == str(employee.departament_id):
            o += 1
    print(o)


def read_employee_id():
    print(angajati)
    try:
        id_angajat = input('Alegeti id-ul unui angajat!')
        if int(id_angajat) in angajati:
            return int(id_angajat)
    except TypeError:
        return  None

def read_departament_id():
    print(departamente)
    try:
        id_departament = input('Alegeti id-ul unui departament!:')
        if int(id_departament) in departamente:
            return int(id_departament)
    except TypeError:
        return None





m = 1
n = 1

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


