n = 1
angajati = {}
angajati[n] = {}
departamente = {}
departamente[n] = {}

begin = None

while begin != 'q':
    if begin == '1':
        angajat = input('Numele angajatului este:')
        angajati[n]['nume'] = angajat
    if begin == '2':
        nume = input('Numele angajatului:')
        if nume == angajat:
            tel = input('Scrieti numarul de telefon:')
            angajati[n]['telefon'] = tel
        else:
            print('NU ESTE NICI UN ANGAJAT CU ACEST NUME')   
    if begin =='3':
        nume_1 = input('Scrieti numele angajatului:')
        if nume_1 == angajat:
            ID_1 = input('Scrieti ID-ul unic:')
            angajati[n]['ID'] = ID_1
        else:
            print('NU ESTE NIMENI CU ACEST NUME!')
    if begin == '4':
        departament = input('Numele departamentului este:')
        departamente[n]['departament'] = departament
    if begin == '5':
        print(departamente)
        dep1 = input('Specificati departamentul:')
        if dep1 == departament:
            ID = input('Scrieti ID-ul unic:')
            departamente[n]['ID'] = ID
        else:
            print('NU ESTE NICI UN DEPARTAMENT CU ACEST NUME')
    if begin == '6':
        print(angajati)
    if begin == '7':
        print(departamente)
  


    print('1:Adauga un nou angajat .')
    print('2:Adaugati un numar de telefon pentru angajat ,specificand numele acestuia')
    print('3:Creati un ID unic pentru fiecare angajat')
    print('4:Adauga un nou departament.')
    print('5:Creati un ID unic pentru fiecare departament')
    print('6:Lista angajati.')
    print('7:Lista departamente.')
    print('Q:Iesire.')
    begin = input('Choose a option!:')








