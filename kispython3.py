# Самое популярное решение

import math

# def main(a, m, b, x):
#     sum = 0
#     for i in range(1, b + 1):
#         proz1 = 1
#         for j in range(1, m + 1):
#             proz2 = 1
#             for c in range(1, a + 1):
#                 proz2 *= c ** 2 - x ** 4 - (j ** 3 + i) ** 3
#             proz1 *= proz2
#         sum += proz1
#     return sum


# 2-е по популярности

# def func2(a, m, b, x, i, j):
#     part_sum = 1
#     for c in range(1, a + 1):
#         part_sum *= c**2 - x**4 - (j**3 + i) ** 3
#     return part_sum
#
#
# def func1(a, m, b, x, i):
#     part_sum = 1
#     for j in range(1, m + 1):
#         part_sum *= func2(a, m, b, x, i, j)
#     return part_sum
#
#
# def main(a, m, b, x):
#     sum_part = sum((func1(a, m, b, x, i) for i in range(1, b + 1)))
#     return sum_part


# 3-е по популярности

# from functools import reduce

# def main(a, m, b, x):
#     indices = [i for i in range(1, b + 1)]
#
#     def compute_value(acc, idx):
#         i = idx
#         return acc + func2(a, m, b, x, i)
#
#     result = reduce(compute_value, indices, 0)
#     return result
#
#
# def func2(a, m, b, x, i):
#     indices = [j for j in range(1, m + 1)]
#
#     def compute_value(acc, idx):
#         j = idx
#         return acc * func3(a, m, b, x, i, j)
#
#     result = reduce(compute_value, indices, 1)
#     return result
#
#
# def func3(a, m, b, x, i, j):
#     indices = [c for c in range(1, a + 1)]
#
#     def compute_value(acc, idx):
#         c = idx
#         return acc * (c ** 2 - x ** 4 - (j ** 3 + i) ** 3)
#
#     result = reduce(compute_value, indices, 1)
#     return result


# 4-e по популярности

# def main(a, m, b, x):
#     result = 0
#     i, c, j = 1, 1, 1
#
#     while i <= b:
#         result1 = 1
#         while j <= m:
#             result2 = 1
#             while c <= a:
#                 result2 *= (c ** 2 - x ** 4 - (j ** 3 + i) ** 3)
#                 c += 1
#             result1 *= result2
#             j += 1
#             c = 1
#         result += result1
#         i += 1
#         j = 1
#
#     return result


# 5-ое по популярности

# def main(a, m, b, x, i=1, j=1, c=1):
#     if i > b:
#         return 0
#     return func2(a, m, b, x, i, j, c) + main(a, m, b, x, i + 1, j, c)
#
#
# def func2(a, m, b, x, i, j, c):
#     answ = 1
#     for j in range(1, m + 1):
#         answ *= func3(a, m, b, x, i, j, c)
#     return answ
#
#
# def func3(a, m, b, x, i, j, c):
#     answ = 1
#     for c in range(1, a + 1):
#         answ *= (c ** 2 - x ** 4 - (j ** 3 + i) ** 3)
#     return answ

