from random import randrange,choice,randint


jednoduche = ['hovnivál','tučňák','malá žába','červík','žížala','malý Totoro','maminka','děda','babička','modrý Totoro','Pórek','meloun']
slozite=['velká žába','medvěd','tygr','straka','velký Totoro','eletroauto','lachtan','robotický vysavač','rádio','počítač','mercedes']

odpoved = 0
vysledek = 0
chci_pokracovat = True

pochvala = ''

# obyčejné počítání 2 čísla
def obyc_2_cisla():

    vysledek = randrange(21)
    prvni_cislo = randrange(21)
    druhe_cislo = vysledek - prvni_cislo
    if druhe_cislo < 0:
        priklad = str(prvni_cislo) + str(druhe_cislo) + '='
    else:
        priklad = str(prvni_cislo) + '+' + str(druhe_cislo) + '='
    odpoved = int(input(priklad))
    while True:
        if odpoved == vysledek:
            break
        else:
            odpoved = int(input(':(  Zkus to spočítat znova: ' + priklad))

# doplňování znamének
def znamenka():
    vysledek = randrange(21)
    prvni_cislo = randrange(21)
    druhe_cislo = vysledek - prvni_cislo
    if druhe_cislo < 0:
        znamenko = ['-']
    elif druhe_cislo > 0:
        znamenko = ['+']
    else: # 0 musí být + i -
        znamenko =  ['+','-']
    print(str(prvni_cislo) + ' ___ ' + str(abs(druhe_cislo)) + '= ' + str(vysledek))
    znamenko_odpoved = input()
    while True:
        if znamenko_odpoved in znamenko:
            #print('())')
            break
        else:
            znamenko_odpoved = input(' (°_°)  Zkus to znova: ' )
    print('\n')

# rovnice o 3 nebo 4 číslech
def rovnice_slozitejsi():
    pocet_cisel = choice([3,4])
    prvni_cislo = randrange(11) # nemůže být záporné, proto je mimo
    suma = prvni_cislo #pozdeji vysledek
    seznam_cisel = [prvni_cislo]
    seznam_znamenek = ['+']
    for _ in range(pocet_cisel - 1):
        cislo = randint(-suma, 10 - suma)
        suma = suma + cislo
        seznam_cisel.append(cislo)
        if cislo < 0:
            seznam_znamenek.append('-')
        else:
            seznam_znamenek.append('+')
    if pocet_cisel == 3:
        rovnice = (str(prvni_cislo) + ' ' + seznam_znamenek[1] + ' ' + str(abs(seznam_cisel[1])) + ' ' + seznam_znamenek[2] + ' ' + str(abs(seznam_cisel[2])) + ' = ' )
    else:
        rovnice = (str(prvni_cislo) + ' ' + seznam_znamenek[1] + ' ' + str(abs(seznam_cisel[1])) + ' ' + seznam_znamenek[2] + ' ' + str(abs(seznam_cisel[2])) + ' ' + seznam_znamenek[3] + ' ' + str(abs(seznam_cisel[3])) + ' = ')
    #odpoved = int(input(rovnice))

    while True:
        while True:
            odpoved = input(rovnice)
            if odpoved.isdigit():
                odpoved = int(odpoved)
                break
            else:
                print('Nanepsal jsi číslo.')
        if odpoved == suma:
            break
        else:
            print(' (°_°) Zkus to znova ...')

#######################################
print('---------------------------------------------')
print('\n\n\n ČAU ... Co budeme spolu trénovat?\n')
while (chci_pokracovat == True):
    print('---------------------------------------------')
    print('Jednoduché příklady - napiš: 1 \n')
    print('Složité příklady - napiš: 2 \n')
    print('Doplňování znamének - napiš: 3 \n')
    print('Jestli na to už prdíš. Napiš: kvak \n')
    print('---------------------------------------------')
    zadani = input()
    if zadani == 'kvak':
        chci_pokracovat = False
        print('Měj se famfárově. :*')
        break
    elif zadani == '1':
        print('Jdeme na to: \n')
        for _ in range (10):
            obyc_2_cisla()
        pochvala = choice(jednoduche)
        print('\n Hotovo. Jsi šikovný jako ' + pochvala + '.\n')
    elif zadani == '2':
        print('Jdeme na to: \n')
        for _ in range (10):
            rovnice_slozitejsi()
        pochvala = choice(slozite)
        print('\n Hotovo. Jsi šikovný jako ' + pochvala + '.\n')
    elif zadani == '3':
        print('Jdeme na to: \n')
        for _ in range (10):
            znamenka()
        print('\n Hotovo. Nejsi náhodou robot, když ti to tak jde? :O \n')
    else:
        print('Zadej 1,2,3 nebo kvak...')
        zadani = input()
    print('\n ---------------------------------------------')
    print('Co budeme dělat dál? \n')

