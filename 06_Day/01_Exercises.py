# Level 1


empty = tuple()
sisters = ('Karely', 'Ximena')
brothers = ('Brian', 'Dani')
siblings = sisters + brothers
print(len(siblings))
family_members = siblings + ('Ramiro', 'Maria de los Angeles')

# Level 2
*sibs, father, mother = family_members
print(sibs)
print(father)
print(mother)

fruits = ('mango', 'fresa')
vegetables = ('zanahoria', 'brocoli')
animal_products = ('queso', 'leche')
food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

food_stuff_lt = food_stuff_lt[:len(food_stuff_lt) // 2] + food_stuff_lt[len(food_stuff_lt) // 2 + 1:]
food_stuff_tp = tuple(food_stuff_lt)
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[len(food_stuff_lt) - 3:]
print(food_stuff_lt)
print(first_three)
print(last_three)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

