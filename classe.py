
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

    def __str__(self):
        return self.name + ',' + str(self.manager_id)

    def __repr__(self):
        return "{name}, {manager_id}".format(name=self.name, manager_id=self.manager_id)




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

    def __str__(self):
        return self.name + ',' + self.telephone_number + ',' + str(self.departament_id)

    def __repr__(self):
        return "{name},{telephone_number},{departament_id}".format(name=self.name,
                                                                   telephone_number=self.telephone_number,
                                                                   departament_id=self.departament_id)



class Product:
    product_current_idx = 1
    items = {}
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
    sale_current_idx = 1
    items = {}
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

