angajati ={}
departamente = {}

begin = None

while begin != '9':
    if begin == '1':
        ang = input('Numele angajatului este:')
        angajati["angajat"]= ang
    if begin == '2':
        nume = input('Numele angajatului:')
        if nume == ang:
            tel = input('Scrieti numarul de telefon:')
            angajati["telefon"] = tel
        else:
            print('NU ESTE NICI UN ANGAJAT CU ACEST NUME')   
    if begin =='3':
        nume_1 = input('Scrieti numele angajatului:')
        ID_1 = input('Scrieti ID-ul unic:')
        angajati["ID"] = ID_1
    if begin == '4':
        dep = input('Numele departamentului este:')
        departamente["Departament"] = dep
    if begin == '5':
        dep1 = input('Specificati departamentul:')
        if dep1 == dep:
            ID = input('Scrieti ID-ul unic:')
            departamente["ID"] =ID 
        else:
            print('NU ESTE NICI UN DEPARTAMENT CU ACEST NUME')
    if begin == '6':
        print(angajati)
    if begin == '7':
        print(departamente)
    if begin =='8':
        print(departamente)
        dep2 = input('Scrieti departamentul pe care il doriti:')
        nume1 = input('Numele angajatului:')
    

    print('1:Adauga un nou angajat .')
    print('2:Adaugati un numar de telefon pentru angajat ,specificand numele acestuia')
    print('3:Creati un ID unic pentru fiecare angajat')
    print('4:Adauga un nou departament.')
    print('5:Creati un ID unic pentru fiecare departament')
    print('6:Lista angajati.')
    print('7:Lista departamente.')
    print('8:Adauga un angajat la un departament')
    print('9:Iesire.')
    begin = input('Choose a option!:')







