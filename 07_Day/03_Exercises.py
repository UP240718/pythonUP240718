# Level 3

#1
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(set(age)) < len(age))
#2
"""
string: es inmutable, es una secuencia ordenada de caracteres, permite caracteres repetidos.
list: es mutable, es ordenada, peremite valores duplicados.
tuple: es inmutable, es ordenada, permite valores duplicados.
sent: es mutable, pero sus elementos deben ser inmutables, no es ordenado, no permite elementos duplicados.
"""
string = "I am a teacher and I love to inspire and teach people."
print(len(set(string.split())))
