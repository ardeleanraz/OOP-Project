def create_users():
    from classe import Employee
    name = input('Numele angajatului este:')
    telephone_number = input('Numarul de telefon al angajatului este:')
    employee = Employee(name, telephone_number, None)

    from classe import Departament
    if Departament.members:
        from read import read_departament_id
        departament_id = read_departament_id()
    else:
        departament_id = None
    employee = Employee(name, telephone_number, departament_id)

    Employee.members[Employee.employee_current_idx] = employee
    Employee.employee_current_idx += 1


def print_users():
    from classe import Employee
    print(Employee.members)




def print_employee_sales():
    from classe import  Employee
    number_of_sales = 0
    print(Employee.members)
    id_employee = input('Alegeti id-ul angajatului pentru care doriti sa vedeti numarul de produse vandute:')

    from sales import Sale
    for sale_id, sale in Sale.items.items():
        if id_employee == str(sale.employee_id):
             number_of_sales += 1
    print(number_of_sales)