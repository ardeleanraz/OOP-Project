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
        return "{name},{telephone_number},{departament_id}".format(name=self.name,
                                                                   telephone_number=self.telephone_number,
                                                                   departament_id=self.departament_id)


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



class Product:
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

    def __str__(self):
        return self.name + str(self.price) + str(self.departament_id)

    def __repr__(self):
        return "{name},{price},{id_departament}".format(name= self.name, price = self.price , id_departament = self.departament_id)



class Sale:
    """Represent any sales"""

    def __init__(self,product_id,year , month, day , employee_id):
        """
        :param int|None product_id : name of product
        :param int|None year: the year of sale
        :param int|None month: the month of sale
        :param int|None day : the day of sale
        :param int|None employee_id: seller id who sell this product

        """
        self.product_id = product_id
        self.year = year
        self.month = month
        self.day = day
        self.employee_id = employee_id



    def __str__(self):
        return self.product_id + self.year + self.month + self.day + self.employee_id


    def __repr__(self):
        return "{product_id},{year}/{month}/{day},{employee_id}".format(product_id =self.product_id , year = self.year,
                                                                        month =self.month , day= self.day ,employee_id =self.employee_id)



def create_sale():
    global x
    if produse:
        product_id = read_product_id()
        year = input('Anul in care s-a fabricat produsul:')
        month = input('Luna in care s-a fabricat produsul:')
        day = input('Ziua in care s-a fabricat produsul:')
        if angajati:
            employee_id = read_employee_id()
        else:
            employee_id = None

        sales = Sale(product_id, int(year), int(month), int(day), employee_id)
        vanzari[x] = sales
        x = x + 1

def create_product():
    global o

    if departamente:
        departament_id = read_departament_id()
        name = input('Numele produsului este:')
        price = input('Pretul produsului este:')

        product = Employee(name , price , departament_id)
        produse[o] = product
        o = o + 1


def create_users():
    global n
    name = input('Numele angajatului este:')
    telephone_number = input('Numarul de telefon al angajatului este:')
    employee = Employee(name, telephone_number, None)
    if departamente:
        departament_id = read_departament_id()
    else:
        departament_id = None
    employee = Employee(name, telephone_number, departament_id)
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

def print_product():
    print(produse)

def print_sales():
    print(vanzari)

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


def read_employee_id():
    print(angajati)
    try:
        angajat_id = input('Alegeti id-ul unui angajat!')
        if int(angajat_id) in angajati:
            return int(angajat_id)
    except TypeError:
        return None


def read_departament_id():
    print(departamente)
    try:
        id_departament = input('Alegeti id-ul unui departament!:')
        if int(id_departament) in departamente:
            return int(id_departament)
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


m = 1
n = 1
o = 1
x = 1
produse = {}
angajati = {}
departamente = {}
vanzari = {}
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

    if begin == '8':
        create_sale()

    if begin == '9':
        print_sales()

    if begin =='10':
        create_product()

    if begin =='11':
        print_product()


    print('1:Adauga un nou angajat .')

    print('2:Adauga un nou departament.')

    print('3:Lista angajati.')

    print('4:Lista departamente.')

    print('5:Listati angajatii in functie de departamente.')

    print('6:Inlocuiti managerul unui departament cu un alt angajat.')

    print('7:Printati numarul de angajati dintr-un departament!')

    print('8:Creati detalii despre o vanzare!')

    print('9:Printati vanzarile !')

    print('10:Creati un nou produs!')

    print('11:Printati produsele!')

    print('Q:Iesire.')

    begin = input('Choose a option!:')




