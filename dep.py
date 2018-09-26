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
        departament_id = input('Alegeti id-ul unui departament din cele existente !:')
        if int(departament_id) in departamente:
            angajati[n]['departament'] = departament_id
        else:
            print('NU AVEM ACEST DEPARTAMENT!')
        n = n +1

    if begin == '2':
        departament = input('Numele departamentului este:')
        departamente[m] = {'nume_departament': departament}
        m = m +1
        
    if begin == '3':
        print(angajati)

    if begin == '4':
        print(departamente)
    
    if begin == '5':
        print(departamente)
        id_departamente = input('Alegeti id-ul pentru care doriti sa printati lista angajatiilor:')
        for  angajat in angajati.values():
            if id_departamente == angajat['departament']:
                print(angajat['nume'])
            else:
                print ('NU AVEM ACEST DEPARTAMENT!')
    
    if begin == '6':
        print(departamente)
        id_departament = input('Alegeti id-ul departamentului din cele existente:')
        print(angajati)
        id_angajat = input('Alegeti id-ul angajatului pe care doriti sa il puneti in functia de manager:')
        if int(id_departament) in departamente and int(id_angajat) in angajati:
            departamente[int(id_departament)]['manager_departament'] = id_angajat
        else:
            print('Nu avem acest departament sau acest angajat!')
    
    if begin =='7':
        print(departamente)
        id_departament = input('Alegeti id-ul departamentului in care se va face schimbarea:')
        print(angajati)
        id_ang = input('Alegeti id-ul unui angajat:')
        departamente[int(id_departament)]['manager_departament'] = id_ang
                    

                 
             
       

    print('1:Adauga un nou angajat .')
    print('2:Adauga un nou departament.')
    print('3:Lista angajati.')
    print('4:Lista departamente.')
    print('5:Listati angajatii in functie de departamente.')
    print('6:Creati un manager pentru fiecare departament.')
    print('7:Inlocuiti managerul unui departament cu un alt angajat.')
    print('Q:Iesire.')
    begin = input('Choose a option!:')


