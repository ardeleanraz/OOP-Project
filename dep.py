angajati = []
departamente = []

begin = None

while begin != '5':
    if begin == '1':
        ang = input('Numele angajatului este:')
        angajati.append(ang)
    if begin == '2':
        print(angajati)
    if begin == '3':
        dep = input('Numele departamentului este:')
        departamente.append(dep)
    if begin == '4':
        print(departamente)

    print('1:Adauga un angajat.')
    print('2:Lista angajati.')
    print('3:Adauga departamente.')
    print('4:Lista departamente.')
    print('5:Iesire.')
    begin = input('Choose a option!:')
