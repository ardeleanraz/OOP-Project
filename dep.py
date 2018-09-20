n = 1
m = 1


angajati ={}
departamente ={}
begin = None


while begin != 'q':
    if begin == '1':
        angajat = input('Numele angajatului este:')
        angajati[n] = {'nume': angajat}
        
        tel = input('Scrieti numarul de telefon:')
        angajati[n]['telefon'] = tel
   
        print(departamente)
        dep_2 = input('Alegeti un departament din cele existente !:')
        if dep_2 in departamente.keys():
            angajati[n]['departament'] = dep_2
        else:
            print('NU AVEM ACEST DEPARTAMENT!')
        n = n +1

    if begin == '2':
        departament = input('Numele departamentului este:')
        departamente[m] = {'departament': departament}
        m = m +1
        
    if begin == '3':
        print(angajati)

    if begin == '4':
        print(departamente)


    print('1:Adauga un nou angajat .')
    print('2:Adauga un nou departament.')
    print('3:Lista angajati.')
    print('4:Lista departamente.')
    print('Q:Iesire.')
    begin = input('Choose a option!:')

