# Level 2
# 1
sum_nums = 0
for a in range(0, 101):
    sum_nums += a
print("The sum of all numbers is", sum_nums)

# 2
even_sum = 0
odd_sum = 0
for a in range(0, 101):
    if a % 2 == 0:
        even_sum += a
    else:
        odd_sum += a
print("The sum of all even numbers is", even_sum)
print("The sum of all odd numbers is", odd_sum)

