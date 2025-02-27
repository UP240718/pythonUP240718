

# Variables in Python

first_name = 'Brian'
last_name = 'Gutiérrez'
full_name = 'Brian Ramiro Gutierrez Gonzalez'
country = 'Jalisco'
city = 'Jalostotitlan'
age = 18
year = 2025
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Brian', 
    'lastname':'Gutierrez', 
    'country':'Jalisco',
    'city':'Jalostotitlan'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Brian', 'Gutierrez', 'Jalisco', 18, 'No'

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#Level 2#

num_one = 5
num_two = 4

Total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print('Total:',num_one + num_two)
print('Diff:',num_two - num_one)
print('Producto:',num_two * num_one)
print('Division:',num_one / num_two)
print('Remainder:',num_one % num_two)
print('Exp:',num_one ** num_two)
print('Floor_Division:',num_one // num_two)

radius = 30
area_of_circle = 3.1416 * radius **2
print('El area es:',area_of_circle) 
circum_of_circle = 3.1416 * radius
print('La circunferencia es:',circum_of_circle)

import math
radius = float(input("Introduce el radio del círculo: "))
area = math.pi * radius ** 2
print(f"El área del círculo es: {area:.2f}")


primer_nombre = input("Introduce tu primer nombre: ")
apellido = input("Introduce tu apellido: ")
pais = input("Introduce tu país: ")
edad = input("Introduce tu edad: ")

print(f"Hola, {primer_nombre} {apellido} de {pais}. Tienes {edad} años.")


help('keywords')