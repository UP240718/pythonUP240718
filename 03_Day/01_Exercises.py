import math

edad = 18
altura = 1.86
numero_complejo = 2 + 3j

# solicitar introducir la base y la altura
base = float(input("ingresa la base del triangulo en metros:"))
altura_triangulo = float(input("ingresa la altura del triangulo en metros:"))

# calcular con formula
area_triangle = 0.5 * base * altura_triangulo
print(f"el area del triamgulo es: {area_triangle} metros cuadrados")

# introducir tres lados del triangulo
a = float(input("introduce al lado a del triangulo:"))
b = float(input("introduce al lado b del triangulo:"))
c = float(input("introduce al lado c del triangulo:"))

#Se calcula el perimetro#
perimeter_triangle = a + b + c
print(f"el perimetro del triangulo es: {perimeter_triangle} ")

#obtener longitud y ancho del rectangulo
length = float(input("inrtoducir la longitud del rectangulo: "))
width = float(input("introduce el ancho del rectangulo: "))

area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print(f"Area del rectangulo: {area_rectangle}")
print(f"perimetro del rectangulo: {perimeter_rectangle}")

radius = float(input("introduce el radio del circulo:"))
pi = 3.1416
area_circle = pi * radius ** 2
circunference = 2 * pi * radius

print(f"area del circulo es igual: {area_circle}")
print(f"circunferencia del circulo: {circunference}")

#calcular la pendiente, la interseccion en "x" y en "y" de la ecuacion y= 2x - 2#
slope = 2 
x_intercept = 2 / 2
y_intercept = -2

print(f"pendiente: {slope}")
print(f"interseccion en x: {x_intercept}")
print(f"interseccion en y: {y_intercept}")

#calcular la pendiente y la distancia euclidiana entre los puntops (2,2) y (6,8)
x1, y1 = 2,2
x2, y2 = 6,8

slope_2 = (y2 - y1) /  (x2 - x1) #fromula de la pendiente
euclidean_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) #distancia euclidiana, no se como salio.

print(f"pendiente entre (2,2) y (6,8): {slope_2}")
print(f"distancia euclidiana: {euclidean_distance}")

#comparar pendientes
if slope == slope_2:
   print("las pendientes son iguales")
else:
   print("las pendientes son diferentes")

#encontrar el valor de x donde y = x^2 + 6x + 9 es 0
# la ecuacion es (x + 3)^2 = 0. por lo que x = -3
def calculate_y(x):
   return x**2 + 6*x +9
x_values = [-5 ,-4, -3, -2, -1, 0]   
for x in x_values:
   print(f"para x = {x}, y = {calculate_y(x)}")

# comparar longitudes de python y dragon con un afirmacion falsa
len_python = len("python")
len_dragon = len("dragon")

print(f"la longitud de python es {len_python}, la longitud de dragon es {len_dragon}")
print(f"¿python es mas largo que dragon? {len_python > len_dragon}") #esto es falso

# paso 13
print('on' in 'python' and 'on' in 'dragon')  # Verifica si "on" está en ambas palabras

# paso 14
print('jargon' in "Espero que este curso no esté lleno de jerga")  # "jargon" significa "jerga"

# paso 15
print('on' not in 'python' and 'on' in 'dragon')  

# 16
print(str(float(len('python'))))  # Convierte la longitud de "python" a flotante y luego a cadena

# 17
numero = int(input('Ingresa un número:'))  
print("Par" if numero % 2 == 0 else "Impar")  # Determina si el número es par o impar

#18
value=int(2.7)
print(7//3 == value)

# 19
print(type('10') == type(10))  

# 20
print(int(9.8) == 10)  # Convierte 9.8 a entero y compara con 10

# 21
horas = int(input('Ingresa las horas:'))  
tasa_por_hora = int(input('Ingresa la tarifa por hora:'))  
print("Ganancia semanal:", horas * tasa_por_hora)  # Calcula la ganancia semanal

# 22
años = int(input('Ingresa años:'))  
print(años * 365 * 24 * 60 * 60) 

# 23
for i in range(1, 6):  
    print(i, i ** 0, i ** 1, i ** 2, i ** 3)  