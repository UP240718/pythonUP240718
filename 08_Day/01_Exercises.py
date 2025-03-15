#1
dog = {}

#2
dog['name'] = 'Max'
dog['color'] = 'cafe'
dog['breed'] = 'pastor aleman'
dog['legs'] = 4
dog['age'] = 4

#3
student = {
    'first_name': 'Jesus',
    'last_name': 'Paz',
    'gender': 'Masculino',
    'age': 33,
    'marital_status': 'Soltero',
    'skills': ['Python', 'SQL'],
    'country': 'México',
    'city': 'Ciudad de México',
    'address': 'Calle 123'
}
#4
length = len(student)
print('Longitud del diccionario student:', length)
#5
skills = student['skills']
print('Skills:', skills)
print('Tipo de dato de skills:', type(skills))
#6
student['skills'].append('Java')
student['skills'].append('HTML')
print('Skills actualizados:', student['skills'])
#7
keys = list(student.keys())
#8
values = list(student.values())
#9
items = list(student.items())
#10
del student['address']
#11
del dog

