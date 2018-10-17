from employee import Employee
from sales import Sale
from departament import Departament
from product import Product


def save_file():
    with open('storage/angajati.txt', 'w') as myfile:
        for key, value in Employee.members.items():
            myfile.write("{},{} \n".format(key, value))

    with open('storage/departamente.txt', 'w') as myfile:
        for key, value in Departament.members.items():
            myfile.write("{},{} \n".format(key, value))

    with open('storage/vanzari.txt', 'w') as myfile:
        for key, value in Sale.members.items():
            myfile.write("{},{} \n".format(key, value))

    with open('storage/produse.txt', 'w') as myfile:
        for key, value in Product.members.items():
            myfile.write("{},{}\n".format(key, value))


def read_file():
    with open('storage/angajati.txt') as myfile:
        for line in myfile:
            key , name, telephone_number, departament_id = line.split(",")
            employee = Employee(name, telephone_number, int(departament_id))
            Employee.members[int(key)] = employee


with open('storage/departamente.txt') as myfile:
    for line in myfile:
        a, b, c = line.split(",")
        key = a
        value = [b, c]
        Departament.members[key] = value

with open('storage/produse.txt') as myfile:
    for line in myfile:
        a, b, c, d = line.split(",")
        key = a
        value = [b, c, d]
        Product.members[key] = value

with open('storage/vanzari.txt') as myfile:
    for line in myfile:
        a, b, c, d, e, f = line.split(",")
        key = a
        value = [b, c, d, e, f]
        Sale.members[key] = value

begin = None
while begin != 'q':
    if begin == '1':
        Employee.create_users()

    if begin == '2':
        Departament.create_departament()

    if begin == '3':
        read_file()
        Employee.print_users()

    if begin == '4':
        read_file()
        Departament.print_departament()

    if begin == '5':
        Departament.print_users_by_dep_id()

    if begin == '6':
        Departament.change_dep_manager()

    if begin == '7':
        Departament.numbers_of_dep_users()

    if begin == '8':
        Sale.create_sale()

    if begin == '9':
        save_file()
        Sale.print_sales()

    if begin == '10':
        Product.create_product()

    if begin == '11':
        save_file()
        Product.print_product()

    if begin == '12':
        Employee.print_employee_sales()

    if begin == '13':
        Departament.print_departament_product()

    if begin == '14':
        Product.most_expensive_product()

    if begin == 's':
        save_file()

    print('1:Adauga un nou angajat .')
    print()
    print('2:Adauga un nou departament.')
    print()
    print('3:Lista angajati.')
    print()
    print('4:Lista departamente.')
    print()
    print('5:Listati angajatii in functie de departamente.')
    print()
    print('6:Inlocuiti managerul unui departament cu un alt angajat.')
    print()
    print('7:Printati numarul de angajati dintr-un departament!')
    print()
    print('8:Creati detalii despre o vanzare!')
    print()
    print('9:Printati vanzarile !')
    print()
    print('10:Creati un nou produs!')
    print()
    print('11:Printati produsele!')
    print()
    print('12:Printati numarul produselor vandute de un  angajat!')
    print()
    print('13:Printati produsele create de un departament!')
    print()
    print('14:Printati pretul cel mai mare dintre produse!')
    print()
    print('S:Salvati datele introduse')
    print()
    print('Q:Iesire.')
    print()
    begin = input('Choose a option!:')
