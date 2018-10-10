from departament import departamente
from read import read_departament_id
from sales import vanzari


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
angajati = {}
n = 1

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


def print_users():
    print(angajati)








def print_employee_sales():
    o = 0
    print(angajati)
    id_employee = input('Alegeti id-ul angajatului pentru care doriti sa vedeti numarul de produse vandute:')

    for sale_id, sale in vanzari.items():
        if id_employee == str(sale.employee_id):
             o += 1
    print(o)