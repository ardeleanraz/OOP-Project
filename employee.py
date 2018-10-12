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


    @staticmethod
    def create_users():

        name = input('Numele angajatului este:')
        telephone_number = input('Numarul de telefon al angajatului este:')
        employee = Employee(name, telephone_number, None)

        from departament import Departament
        if Departament.members:
            from read import read_departament_id
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
        for sale_id, sale in Sale.items.items():
            if id_employee == str(sale.employee_id):
                number_of_sales += 1
        print(number_of_sales)



    def __str__(self):
        return self.name + ',' + self.telephone_number + ',' + str(self.departament_id)

    def __repr__(self):
        return "{name},{telephone_number},{departament_id}".format(name=self.name,
                                                                   telephone_number=self.telephone_number,
                                                                   departament_id=self.departament_id)




