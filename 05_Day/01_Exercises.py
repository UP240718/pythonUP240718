#Level 1

#1
empty_list = []
#2
my_list = [1, 2, 3, 4, 5, 6]
#3
list_length = len(my_list)
print("Longitud ed la lista:", list_length)
#4
first_item = my_list[1]
middle_item = my_list[len(my_list) // 2]
last_item = my_list[-1]
print("primer elemento:", list_length)
print("elemento del medio", middle_item)
print("ultimo elemento", last_item)
#5
mixed_data_types = ["TuNombre", 25, 1.75, "Soltero", "Tu Dirección"]
print("Lista de datos mixtos:", mixed_data_types)

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7
print("Lista de empresas de TI:", it_companies)

#8
print("Número de empresas:", len(it_companies))

#9
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]

print("Primera empresa:", first_company)
print("Empresa del medio:", middle_company)
print("Última empresa:", last_company)

#10
it_companies[2] = "Tesla"
print("Lista después de modificar:", it_companies)

#11
it_companies.append("Netflix")
print("Lista después de agregar una empresa:", it_companies)

#12
it_companies.insert(len(it_companies) // 2, "Intel")
print("Lista después de insertar en el medio:", it_companies)

#13
it_companies[1] = it_companies[1].upper()
print("Lista después de modificar a mayúsculas:", it_companies)

#14
joined_companies = "#;  ".join(it_companies)
print("Empresas unidas:", joined_companies)

#15
company_to_check = "Google"
exists = company_to_check in it_companies
print(f"¿{company_to_check} está en la lista?:", exists)

#16
it_companies.sort()
print("Lista ordenada:", it_companies)

#17
it_companies.reverse()
print("Lista en orden inverso:", it_companies)

#18
first_three = it_companies[:3]
print("Primeras tres empresas:", first_three)

#19
last_three = it_companies[-3:]
print("Últimas tres empresas:", last_three)

#20
it_companies = it_companies[0:len(it_companies) // 2] + it_companies[len(it_companies) // 2 + 1:]

#21
it_companies.pop(0)
print("Lista después de eliminar la primera empresa:", it_companies)

#22
it_companies.pop(len(it_companies) // 2)

#23
it_companies.pop()
print("Lista después de eliminar la última empresa:", it_companies)

#24
it_companies.clear()
print("Lista después de eliminar todas las empresas:", it_companies)

#25
del it_companies
#print(it_companies)  # Esto generaría un error porque la lista ya no existe

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print("Lista combinada de frontend y backend:", full_stack)

#27
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print("Lista final con Python y SQL agregados:", full_stack)

