# Write a python program to sum of the first n positive integers.

# Sum of first n positive integers can be calculated using the formula: n * (n + 1) // 2

n = int(input("Enter n: "))

sum_n = n * (n + 1) // 2

print(f'Sum of first {n} positive integers is: {sum_n}')