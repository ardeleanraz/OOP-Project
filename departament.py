def create_departament():
    from classe import Departament
    name = input('Numele departamentului este:')
    departament = Departament(name, None)

    from classe import Employee
    if Employee.members:
        from read import read_employee_id
        manager_id = read_employee_id()
    else:
        manager_id = None
    departament = Departament(name, manager_id)
    Departament.members[Departament.departament_current_idx] = departament
    Departament.departament_current_idx += 1




def print_departament():
    from classe import Departament
    print(Departament.members)




def print_departament_product():
    from classe import Departament
    product_dep = []
    print(Departament.members)
    id_departament = input('Alegete id-ul unui departament pentru care doriti sa vedeti produsele :')

    from classe import Product
    for product_id , product in Product.items.items():
        if id_departament in str(product.departament_id):
            product_dep.append(product.name)

    print(product_dep)



def print_users_by_dep_id():
    from classe import Departament

    print(Departament.members)
    id_departament = input('Alegeti id-ul unui departament!:')

    from classe import Employee
    for employee_id, employee in Employee.members.items():
        if id_departament == str(employee.departament_id):
            print(employee.name)



def change_dep_manager():

    from read import read_departament_id
    id_departament = read_departament_id()

    from read import read_employee_id
    employee_id = read_employee_id()

    from classe import  Departament
    Departament.members[id_departament].manager_id = employee_id




def numbers_of_dep_users():
    from classe import Departament
    o = 0

    print(Departament.members)
    id_departament = input('Alegeti id-ul departamentului pentru care doriti sa vedeti numarul de angajati !:')

    from classe import Employee
    for employee_id, employee in Employee.members.items():
        if id_departament == str(employee.departament_id):
            o += 1
    print(o)
