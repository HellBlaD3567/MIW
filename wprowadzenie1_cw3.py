# *****************************
# * @author Kamil Tanasiewicz *
# * @indeks 147332            *
# *****************************

# 1.

print('1. Ten tekst jest na środku \n {:^24} \n'.format('Hello World!'))

# 2.

print("2. {:04d}".format(241));

# 3.

class Person(object):
    name = "Kamil"
    surname = "Tanasiewicz"

print("3. Person: {p.name}, {p.surname}".format(p=Person()))


# 4.

print('4. {:15.8}'.format('Lorem ipsum dolor set enum'))

#5.

print('5. {:_<20}'.format('Ala ma kota'))