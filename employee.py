from Dep_class_object import read_departament_id


class Employee:
    employee_current_idx = 1
    members = {}
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


    def read_employee_id():

        print(Employee.members)
        try:
            angajat_id = input('Alegeti id-ul unui angajat!')
            if int(angajat_id) in Employee.members:
                return int(angajat_id)
        except TypeError:
            return None


    @staticmethod
    def create_users():

        name = input('Numele angajatului este:')
        telephone_number = input('Numarul de telefon al angajatului este:')
        employee = Employee(name, telephone_number, None)

        from departament import Departament
        if Departament.members:

            departament_id = read_departament_id()
        else:
            departament_id = None
        employee = Employee(name, telephone_number, departament_id)

        Employee.members[Employee.employee_current_idx] = employee
        Employee.employee_current_idx += 1



    def print_users():
        print(Employee.members)

    def print_employee_sales():

        number_of_sales = 0
        print(Employee.members)
        id_employee = input('Alegeti id-ul angajatului pentru care doriti sa vedeti numarul de produse vandute:')

        from sales import Sale
        for sale_id, sale in Sale.members.items():
            if id_employee == str(sale.employee_id):
                number_of_sales += 1
        print(number_of_sales)



    def __str__(self):
      return 'Name:' + self.name + ',' + 'Telephone_Number:' +self.telephone_number + ',' +'Departament_id: ' + str(self.departament_id)

    def __repr__(self):
        return "{name},{telephone_number},{departament_id}".format(name=self.name,
                                                                   telephone_number=self.telephone_number,
                                                                   departament_id=self.departament_id)




