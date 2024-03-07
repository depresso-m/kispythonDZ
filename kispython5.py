# Самое популярное решение

# from math import ceil
#
# def main(z, y):
#     n = len(z)
#     y.insert(0, 0)
#     z.insert(0, 0)
#     summa = 0
#     for i in range(1, n + 1):
#         left = 1 + 51 * z[n + 1 - ceil(i / 2)]
#         right = 45 * pow(y[n + 1 - ceil(i / 2)], 3)
#         summa += (left + right) ** 5
#     return 49 * summa


# 2-е по популярности

# def main(z, y):
#     n = len(z)
#     z = [0] + z
#     y = [0] + y
#     summa = sum((1 + 51 * z[n + 1 - (i + 1) // 2] + 45 *
#                  (y[n + 1 - (i + 1) // 2] ** 3)) ** 5 for i in range(1, n + 1))
#     return 49 * summa

# 3-е по популярности

# from math import ceil
#
#
# def main(z, y):
#     n = len(z)
#     y.insert(0, 0)
#     z.insert(0, 0)
#     summa = 0
#     i = 1
#     while i <= n:
#         left = 1 + 51 * z[n + 1 - ceil(i / 2)]
#         right = 45 * pow(y[n + 1 - ceil(i / 2)], 3)
#         summa += (left + right) ** 5
#         i += 1
#     return 49 * summa

# 4-е по популярности

# from math import ceil
#
#
# def calculate_sum_recursive(z, y, i, n, acc):
#     if i > n:
#         return acc
#     left = 1 + 51 * z[n + 1 - ceil(i / 2)]
#     right = 45 * pow(y[n + 1 - ceil(i / 2)], 3)
#     acc += (left + right) ** 5
#     return calculate_sum_recursive(z, y, i + 1, n, acc)
#
#
# def main(z, y):
#     n = len(z)
#     y.insert(0, 0)
#     z.insert(0, 0)
#     return 49 * calculate_sum_recursive(z, y, 1, n, 0)
