class Departament:
    departament_current_idx = 1
    members = {}
    """ Represents any departament."""

    def __init__(self, name, manager_id):
        """
        :param str name:  name of the department
        :param int|None manager_id: the ID of an employee, which is the manager of this department
        """
        self.name = name
        self.manager_id = manager_id

    @staticmethod
    def create_departament():

        name = input('Numele departamentului este:')
        departament = Departament(name, None)

        from employee import Employee
        if Employee.members:

            from read import read_employee_id
            manager_id = read_employee_id()
        else:
            manager_id = None
        departament = Departament(name, manager_id)
        Departament.members[Departament.departament_current_idx] = departament
        Departament.departament_current_idx += 1




    def print_departament():

            print(Departament.members)

    def print_departament_product():
            product_dep = []
            print(Departament.members)
            id_departament = input('Alegete id-ul unui departament pentru care doriti sa vedeti produsele :')

            from product import Product
            for product_id, product in Product.members.items():
                if id_departament in str(product.departament_id):
                    product_dep.append(product.name)

            print(product_dep)

    def print_users_by_dep_id():

            print(Departament.members)
            id_departament = input('Alegeti id-ul unui departament!:')

            from employee import Employee
            for employee_id, employee in Employee.members.items():
                if id_departament == str(employee.departament_id):
                    print(employee.name)

    def change_dep_manager():

            from read import read_departament_id
            id_departament = read_departament_id()

            from read import read_employee_id
            employee_id = read_employee_id()

            Departament.members[id_departament].manager_id = employee_id

    def numbers_of_dep_users():

            o = 0

            print(Departament.members)
            id_departament = input('Alegeti id-ul departamentului pentru care doriti sa vedeti numarul de angajati !:')

            from employee import Employee
            for employee_id, employee in Employee.members.items():
                if id_departament == str(employee.departament_id):
                    o += 1
            print(o)

    def __str__(self):
        return  self.name + ',' + str(self.manager_id)

    def __repr__(self):
        return "{name}, {manager_id}".format(name=self.name, manager_id=self.manager_id)



