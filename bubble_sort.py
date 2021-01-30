# definovani funkci

# zjisteni, zda se jedna o cislo nebo o text
def zda_cislo(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

# nacteni dat ze souboru vstup.txt
def nacist_cisla():
    try:
        with open('vstup.txt', 'r') as h:
            obsah = h.readlines() 
        sez_cisla = []
        for radek in obsah:
            # pokud je oddelovac carka, vymenime ji za mezeru
            radek.replace(',',' ')
            # rozdelime radek na casti podle mezer
            for i in radek.split(): 
                # pokud polozka v radku je cislo, pridame do seznamu cisel
                if zda_cislo(i) == True: 
                    sez_cisla.append(float(i))
        return sez_cisla
    except FileNotFoundError:
        exit("Nenalezen vstupní soubor vstup.txt")
    except PermissionError:
        exit("Nemám přístup k vstupnímu souboru vstup.txt")

# ulozeni setridenych cisel do vystup.txt
def uloz_cisla(setridena):
    try:
        with open('vystup.txt','w') as k:
            for i in setridena:
                k.write("{:g} ".format(i))
    except PermissionError:
        exit("Nemám přístup k výstupnímu souboru vystup.txt")

# hlavni cast programu

# nacteni dat
cisla = nacist_cisla()
# setrideni cisel metodou bubble sort
p=0
while p == 0:
    p = 1
    for i in range(len(cisla)-1):
        if cisla[i]<cisla[i+1]:
            a=cisla[i]
            cisla[i]=cisla[i+1]
            cisla[i+1]=a
            p=0
# export setridenych cisel
uloz_cisla(cisla)