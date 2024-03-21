# Самое популярное решение

# def zero(items, left, right):
#     if items[0] == 1987:
#         return right
#     if items[0] == 1984:
#         return left
#
#
# def one(items, left, right):
#     if items[1] == 2015:
#         return right
#     if items[1] == 1971:
#         return left
#
#
# def two(items, left, midd, right):
#     if items[2] == 1964:
#         return right
#     if items[2] == 2004:
#         return midd
#     if items[2] == 1997:
#         return left
#
#
# def three(items, left, midd, right):
#     if items[3] == 2005:
#         return right
#     if items[3] == 1993:
#         return midd
#     if items[3] == 1960:
#         return left
#
#
# def main(items):
#     result = zero(items, three(items, one(items, 10, 9), 8, 7), two(items, three(items, 6, 5, 4), 3, three(items, 2, 1, 0)))
#     return result


# 2-ое по популярности решение

# s = (
#     {1987, 1964, 2005},
#     {1987, 1964, 1993},
#     {1987, 1964, 1960},
#     {1987, 2004},
#     {1987, 1997, 2005},
#     {1987, 1997, 1993},
#     {1987, 1997, 1960},
#     {1984, 2005},
#     {1984, 1993},
#     {1984, 1960, 2015},
#     {1984, 1960, 1971}
# )
#
# def main(r):
#     s1 = set(r)
#     return [i for i in range(len(s)) if not (len(s[i] - s1))][0]


# 3-ое по популяности решение

# def zero(items, left, right):
#     match items[0]:
#         case 1987:
#             return right
#         case 1984:
#             return left
#
#
# def one(items, left, right):
#     match items[1]:
#         case 2015:
#             return right
#         case 1971:
#             return left
#
#
# def two(items, left, mid, right):
#     match items[2]:
#         case 1964:
#             return right
#         case 2004:
#             return mid
#         case 1997:
#             return left
#
#
# def three(items, left, mid, right):
#     match items[3]:
#         case 2005:
#             return right
#         case 1993:
#             return mid
#         case 1960:
#             return left
#
#
# def main(items):
#     result = zero(
#         items,
#         three(items, one(items, 10, 9), 8, 7),
#         two(items, three(items, 6, 5, 4), 3, three(items, 2, 1, 0)),
#     )
#     return result


# 4-ое по популярности решение

# s = (
#     {1987, 1964, 2005},
#     {1987, 1964, 1993},
#     {1987, 1964, 1960},
#     {1987, 2004},
#     {1987, 1997, 2005},
#     {1987, 1997, 1993},
#     {1987, 1997, 1960},
#     {1984, 2005},
#     {1984, 1993},
#     {1984, 1960, 2015},
#     {1984, 1960, 1971}
# )
#
# def main(items):
#     s1 = set(items)
#     for i, v in enumerate(s):
#         if not(len(v - s1)):
#             return i


# 5-ое по популярности решение

# class tree():
#     def __init__(self, number, top, topcon, mid, midcon, down, downcon):
#         self.number = number
#         self.top = top
#         self.mid = mid
#         self.down = down
#         self.topCon = topcon
#         self.midCon = midcon
#         self.downCon = downcon
#
#     def find(self, mas: list, ):
#         if self.top == mas[self.number]:
#             if (type(self.topCon) == int):
#                 return self.topCon
#             return self.topCon.find(mas)
#         if self.mid == mas[self.number]:
#             if (type(self.midCon) == int):
#                 return self.midCon
#             return self.midCon.find(mas)
#         if self.down == mas[self.number]:
#             if (type(self.downCon) == int):
#                 return self.downCon
#             return self.downCon.find(mas)
#
#
# def main(mas):
#     x01 = tree(0,"DART", 0, None, None, "FLUX", 1)
#     x02 = tree(0,"DART", 2, None, None, "FLUX", 3)
#     x03 = tree(0,"DART", 4, None, None, "FLUX", 5)
#     x2 = tree(2,"ELM", 6, "VALA", 7, "OOC", 8)
#     x3 = tree(3,"HLSL", x01, "TEA", x02, "VHDL", x03)
#     x4 = tree(4,"P4", x3, "CSS", x2, "TERRA", 9)
#     x1 = tree(1,1976, x4, None, None, 1988, 10)
#
#     x31 = tree(3, 2005, 0, 1993, 1, 1960, 2)
#     x32 = tree(3, 2005, 4, 1993, 5, 1960, 6)
#     x1 = tree(1, 2015, 9, None, None, 1971, 10)
#     x2 = tree(2, 1964, x31, 2004, 3, 1997, x32)
#     x33 = tree(3, 2005, 7, 1993, 8, 1960, x1)
#     x0 = tree(0, 1987, x2, None, None, 1984, x33)
#     return x0.find(mas)