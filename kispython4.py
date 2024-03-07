# Самое популярное решение

# def main(n):
#     if n == 0:
#         return -0.91
#     elif n == 1:
#         return -0.04
#     elif n >= 2:
#         return ((0.01 - (main(n - 1) ** 2) - (main(n - 1) ** 3)) ** 3 -
#                 (main(n - 2) ** 2))


# 2-е по популярности

# def main(n):
#     a, b = -0.91, -0.04
#     for _ in range(n):
#         a, b = b, (0.01 - (b ** 2) - (b ** 3)) ** 3 - (a ** 2)
#     return a


# 3-е по популярности

# def main(n):
#     v = [-0.91, -0.04]
#
#     for i in range(2, n + 1):
#         v.append(
#             (0.01 - v[i - 1] ** 2 - v[i - 1] ** 3) ** 3 - v[i - 2] ** 2
#         )
#
#     return v[n]


# 4-е по поулярности

# def main(n):
#     sign = n
#     match sign:
#         case 0:
#             return -0.91
#         case 1:
#             return -0.04
#     return (0.01 - main(n - 1) ** 2 - main(n - 1) ** 3) ** 3 - main(n - 2) ** 2


# 5-е по популярности

# def main(n):
#     return (
#         -0.91
#         if n == 0
#         else -0.04
#         if n == 1
#         else (lambda x: (0.01 - x[0] ** 2 - x[1] ** 3) ** 3 - x[2] ** 2)(
#             [main(n - 1), main(n - 1), main(n - 2)]
#         )
#     )
import math