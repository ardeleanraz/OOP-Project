from departament import create_departament, print_departament, print_users_by_dep_id, change_dep_manager, \
    numbers_of_dep_users, print_departament_product
from employee import create_users, print_users, print_employee_sales
from product import create_product, print_product, most_expensive_product
from sales import create_sale, print_sales



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

    if begin =='12':
        print_employee_sales()

    if begin == '13':
        print_departament_product()

    if begin =='14':
        most_expensive_product()




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
    print('Q:Iesire.')
    print()
    begin = input('Choose a option!:')