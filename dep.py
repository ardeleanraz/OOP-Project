angajati = []
departamente = []
departamente_angajati=[]

begin = None

while begin != 'q':
    if begin == '1':
        angajat = input('Numele angajatului este:')
        angajati.append({"nume":angajat})
    if begin == '2':
        nume = input('Numele angajatului:')
        if nume == angajat:
            tel = input('Scrieti numarul de telefon:')
            angajati.append({"telefon":tel})
        else:
            print('NU ESTE NICI UN ANGAJAT CU ACEST NUME')   
    if begin =='3':
        nume_1 = input('Scrieti numele angajatului:')
        if nume_1 == angajat:
            ID_1 = input('Scrieti ID-ul unic:')
            angajati.append({"ID":ID_1})
        else:
            print('NU ESTE NIMENI CU ACEST NUME!')
    if begin == '4':
        departament = input('Numele departamentului este:')
        departamente.append({"departament":departament})
    if begin == '5':
        dep1 = input('Specificati departamentul:')
        if dep1 == departament:
            ID = input('Scrieti ID-ul unic:')
            departamente.append({"ID":ID}) 
        else:
            print('NU ESTE NICI UN DEPARTAMENT CU ACEST NUME')
    if begin == '6':
        print(angajati)
    if begin == '7':
        print(departamente)
    if begin =='8':
        print(departamente)
        dep2 = input('Scrieti departamentul pe care il doriti:')  
        print(angajati)   
        nume1 = input('Numele angajatului:')
        departamente_angajati.append({dep2:nume1})
    if begin == '9':
        print(departamente_angajati)
      

    print('1:Adauga un nou angajat .')
    print('2:Adaugati un numar de telefon pentru angajat ,specificand numele acestuia')
    print('3:Creati un ID unic pentru fiecare angajat')
    print('4:Adauga un nou departament.')
    print('5:Creati un ID unic pentru fiecare departament')
    print('6:Lista angajati.')
    print('7:Lista departamente.')
    print('8:Adauga un angajat la un departament')
    print('9:Angajatii sortati pe departamente')
    print('Q:Iesire.')
    begin = input('Choose a option!:')










