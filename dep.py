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
        if dep_2 == departament:
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


