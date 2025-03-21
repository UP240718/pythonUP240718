# Level 1

# 1
def add_two_numbers(a, b):
    return a + b


# 2
def area_of_circle(r):
    return 3.14 * r * r


# 3
def add_all_nums(arr):
    sum_of_nums = 0
    for r in arr:
        if isinstance(r, int):
            sum_of_nums += r
    return sum_of_nums


# 4
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# 5
def check_season(month):
    if month in ["September", "October", "November"]:
        print("Autumn")
    if month in ["December", "January", "February"]:
        print("Winter")
    if month in ["March", "April", "May"]:
        print("Spring")
    else:
        print("Summer")


# 6
def calculate_slope(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m


# 7
# noinspection PyPep8Naming
def solve_quadratic_eqn(a, b, c):
    D = b * b - 4 * a * c
    X1 = (-b + D) / (2 * a)
    X2 = (-b - D) / (2 * a)
    print(X1, X2)


# 8
def print_list(lst):
    for r in lst:
        print(r)


# 9
def reverse_list(a):
    return a[::-1]


# 10
def capital_list_terms(a):
    for r in a:
        a[a.index(r)] = r.capitalize()
    return a


# 11
def add_item(mutable, tba):
    mutable.append(tba)
    return mutable


# 12
def remove_item(mutable, tbr):
    mutable.remove(tbr)
    return mutable


# 13
def sum_of_numbers(high):
    sum_of_numbers = 0
    for r in range(high + 1):
        sum_of_numbers += r
    return sum_of_numbers


# 14
def sum_of_odds(high):
    sum_of_odd_nums = 0
    for r in range(high + 1):
        if r % 2 == 1:
            sum_of_odd_nums += r
    return sum_of_odd_nums


# 15
def sum_of_even(high):
    sum_of_even_nums = 0
    for r in range(high + 1):
        if r % 2 == 0:
            sum_of_even_nums += r
    return sum_of_even_nums
