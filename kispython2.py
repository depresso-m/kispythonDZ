# Самое популярное решение

# import math
#
# def main(y):
#     if y < 51:
#         return (1 - 55 * y - pow(y, 3)) ** 3 / 59
#     elif 51 <= y < 80:
#         return 5 * pow(y, 5) - 78 * y
#     elif 89 <= y < 109:
#         return 4 * pow(math.asin(96 * y - pow(y, 3)), 6) + \
#                58 * pow(math.log10(y), 7) + pow(y, 3)
#     elif 109 <= y < 172:
#         return 81 * pow(y, 5) + 1
#     elif y >= 172:
#         return 59 * y


# 2-е по популярности

# from math import asin, log10
#
# def main(y):
#     return (
#         pow((1 - 55 * y - pow(y, 3)), 3) / 59
#         if y < 51
#         else 5 * pow(y, 5) - 78 * y
#         if 51 <= y < 89
#         else 4 * pow(asin(96 * y - pow(y, 3)))
#         + 58 * pow(log10(y), 7)
#         + pow(y, 3)
#         if 89 <= y < 109
#         else func1(y)
#     )
#
#
# def func1(y):
#     return 81 * pow(y, 5) + 1 if 109 <= y < 172 else 59 * y


# 3-е по популярности

# from math import asin, log10
#
# def main(y):
#     funcs = {
#         "case1": lambda y: pow((1 - 55 * y - pow(y, 3)), 3) / 59,
#         "case2": lambda y: 5 * pow(y, 5) - 78 * y,
#         "case3": lambda y: 4 * pow(asin(96 * y - pow(y, 3)))
#         + 58 * pow(log10(y), 7)
#         + pow(y, 3),
#         "case4": lambda y: 81 * pow(y, 5) + 1,
#         "case5": lambda y: 59 * y,
#     }
#
#     if y < 51:
#         return funcs["case1"](y)
#     elif 51 <= y < 89:
#         return funcs["case2"](y)
#     elif 89 <= y < 109:
#         return funcs["case3"](y)
#     elif 109 <= y < 172:
#         return funcs["case4"](y)
#     else:
#         return funcs["case5"](y)