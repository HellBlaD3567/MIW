# *****************************
# * @author Kamil Tanasiewicz *
# * @indeks 147332            *
# *****************************

# ćwiczenie 1

tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym.  Został po raz pierwszy użyty w XV w. " \
        "przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, " \
        "pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty " \
        "Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach " \
        "osobistych, jak Aldus PageMaker"

# ćwiczenie 2

imie = "Kamil"
nazwisko = "Tanasiewicz"
litera_1 = imie[2]
litera_2 = nazwisko[3]

suma_1 = tekst.count(litera_1);
suma_2 = tekst.count(litera_2);

print("W tekście jest %i liter %s oraz %i liter %s" % (suma_1,litera_1,suma_2,litera_2))


# ćwiczenie 3 -> wprowadzenie_cw3.py

# ćwiczenie 4

print(dir(tekst))
help(tekst.splitlines)


# ćwiczenie 5

person = '{} {}'.format(imie, nazwisko);
print(person[::-1].title());

# ćwiczenie 6

lista = list(range(1,11));

nowa_lista = lista[5:]

lista = lista[:5]

print(lista);
print(nowa_lista);

# ćwiczenie 7

lista.extend(nowa_lista);
lista.insert(0, 0);

kopia_lista = lista.copy();
kopia_lista.sort(reverse=True)
print(kopia_lista);

# ćwiczenie 8

lista_studentow = [(157122, 'Kowalski Jan'), (157144, 'Nowak Anna'), (149142, 'Janicki Bartosz')]

# ćwiczenie 9

lista_studentow_slownik = dict(lista_studentow)

print(lista_studentow_slownik)

# ćwiczenie 10

lista_telefonow = ["501 601 701","502 602 702","701 601 501","502 602 702","501 601 701","501 601 703"]
zbior_telefony = set(lista_telefonow)
print(zbior_telefony)

# ćwiczenie 11
for i in range(1,11):
    print(i)

# ćwiczenie 12
for i in range(100 ,15, 5):
    print(i)

# ćwiczenie 13
