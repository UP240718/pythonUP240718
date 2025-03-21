# profe el error que me da a que se debe?

# Level 1
# 1
print("with for:")
for a in range(0, 11):
    print(a)
print("with while:")
b = 0
while b <= 10:
    print(b)
    b += 1

# 2
print("with for:")
for a in range(10, -1, -1):
    print(a)
print("with while:")
b = 10
while b >= 0:
    print(b)
    b -= 1

# 3
print("triangle")
hash_string = '#'
for a in range(1, 8):
    print(hash_string * a)

# 4
print("square")
for a in range(1, 9):
    for r in range(1, 9):
        print("#", end=' ')
    print()

# 5
print("pattern")
for a in range(0, 11):
    print(a, "x", a, "=", a * a)

# 6
print("list")
for lang in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(lang)


# 7
for a in range(0, 101):
    if a % 2 == 0:
        print(a)

# 8
for a in range(0, 101):
    if a % 2 != 0:
        print(a)



