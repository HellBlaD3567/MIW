# *****************************
# * @author Kamil Tanasiewicz *
# * @indeks 147332            *
# *****************************
from file_manager import FileManager
# ćwiczenie 1

a_list = ['a','b','c','d','e','f']
b_list = [1,2,3,4,5,6]

def kombinacja(a_list, b_list):

    c_list = []

    c_list.extend(a_list[1::2])
    c_list.extend(b_list[1::2])

    return c_list

c_list = kombinacja(a_list,b_list)
print('#1')
print(c_list)

# ćwiczenie 2
def textinfo(data_text):


    return {
        "length": len(data_text),
        "letters": set(data_text),
        "big_letters": data_text.upper(),
        'small_letters': data_text.lower()
    }

print('#2')
print(textinfo('Lorem ipsum dolor set enum'))

# ćwiczenie 3
def usun(text,letter):
    for l in text:
        text =  text.replace(letter, "")

    return text

print('#3')
print(usun('Lorem ipsum dolor set enum', 'or'))

# ćwiczenie 4
def przeliczTemperature(temperature, type):
    if(temperature < -273.15):
        return 'Taka temperatura nie istnieje'

    if(type == 'Fahrenheit'):
        return temperature * 1.8 + 32
    elif(type == 'Rankine'):
        return przeliczTemperature(temperature, 'Kelvin') * 1.8
    elif(type == 'Kelvin'):
        return temperature + 273.15
    else:
        return 'Nie znam jednostki'

def wyswieTemperature(temperature, type):
    return str(przeliczTemperature(temperature, type)) + " "+type

print('#4')
print(wyswieTemperature(42, "Rankine"))
print(wyswieTemperature(42, "Kelvin"))
print(wyswieTemperature(42, "Fahrenheit"))

# ćwiczenie 5
class Calculator:
    def add(self, x, y):
        return x+y
    def difference(self, x, y):
        return x-y
    def multiply(self, x, y):
        return x*y
    def divide(self, x,y):
        return x/y

# ćwiczenie 6
class ScienceCalculator(Calculator):
    def pow(self, x, a):
        return x^a

# ćwiczenie 7
def inverse(text):
    return text[::-1]
print('#7')
print(inverse('Ala ma kota'))

# ćwiczenie 9
plik = FileManager("pliczek.txt")
print("Przed zapisem: {}".format(plik.read()))
plik.write('Abecadło 1234')
print("Po zapisie: {}".format(plik.read()))
