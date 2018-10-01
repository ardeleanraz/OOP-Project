class Employee:
    """Represents any departament member. """

    def __init__(self, name, telephone_number, employee_id):
        """
        :param str name: The name of the employee
        :param str telephone_number: The telephone number of an employee
        :param int departament_id: the ID of the department that this employee works in
        """
        self.name = name
        self.telephone_number = telephone_number
        self.employee_id = employee_id


class Departament:
    """ Represents any departament."""

    def __init__(self, name , manager_id):
        """
        :param str name:  name of the department
        :param int manager_id: the ID of an employee, which is the manager of this department
        """
        self.name = name
        self.manager_id = manager_id



n = 1
m = 1
o=1
angajati = {}
departamente = {}
begin = None
while begin != 'q':
    # CREAZA UN ANGAJAT CU DETALII DESPRE ACESTA
    if begin == '1':
        name = input('Numele angajatului este:')
        telephone_number = input('Numarul de telefon al angajatului este:')
        employee_id = input('ID-ul angajatului este:')
        employee = Employee( name,  telephone_number,  int(employee_id))
        angajati[n] = employee
        n = n + 1

    if begin == '2':
        departament_name = input('Numele departamentului este:')
        for employee_id , employee in angajati.items():
            print(employee_id ,':','name:',employee.name, ',' , 'telephone_number:',employee.telephone_number, ',' , 'ID:', employee.employee_id)
        manager_id = input('Alegeti id-ul un angajat pe care doriti sa il puneti in functia de manager:')
        departament = Departament(departament_name, int(manager_id))
        departamente[m] = departament  
        m = m +1

    if begin == '3':
        for employee_id , employee in angajati.items():
            print('name:',employee.name, ',' , 'telephone_number:',employee.telephone_number, ',' , 'departament_ID:', employee.employee_id)

    if begin == '4':
        for departament_id , departament in departamente.items():
            print('departament_name:',  departament.name , ',' , 'Departament_manager:', departament.manager_id)

    if begin == '5':
        for departament_id , departament in departamente.items():
            print(departament_id,':' , 'departament_name:',  departament.name , ',' , 'Departament_manager:', departament.manager_id)
  
        id_departament = input('Alegeti id-ul unui departament!:')
        for  employee_id , employee in angajati.items():
            if id_departament == str(employee.employee_id):
                print(employee.name)
        



    print('1:Adauga un nou angajat .')
    print('2:Adauga un nou departament.')
    print('3:Lista angajati.')
    print('4:Lista departamente.')
    print('5:Listati angajatii in functie de departamente.')
    print('6:Inlocuiti managerul unui departament cu un alt angajat.')
    print('Q:Iesire.')
    begin = input('Choose a option!:')

