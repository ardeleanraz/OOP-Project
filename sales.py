from product import produse
from read import read_product_id, read_employee_id


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


x = 1
vanzari = {}



def create_sale():
    global x
    if produse:
        product_id = read_product_id()
        year = input('Anul in care s-a fabricat produsul:')
        month = input('Luna in care s-a fabricat produsul:')
        day = input('Ziua in care s-a fabricat produsul:')

        from employee import angajati
        if angajati:
            employee_id = read_employee_id()
        else:
            employee_id = None

        sales = Sale(product_id, int(year), int(month), int(day), employee_id)
        vanzari[x] = sales
        x = x + 1


def print_sales():
    print(vanzari)