# from math import floor
#
#
# def calc(K1):
#     answ = 0
#     for kek in K1:
#         answ += kek ** 2
#     return answ
#
#
# def main(input_set):
#     # вычисляем Z
#     Z1 = {b % 2 + abs(b) for b in input_set if (b < 96 or b >= -69)}
#     # вычисляем K
#     K1 = {l1 for l1 in Z1 if ((l1 > -63) ^ (l1 < 26))}
#     # вычисляем O
#     O1 = {b ** 3 + floor(b / 7) for b in input_set if ((b <= 71) ^ (b > -66))}
#     answ = abs(len(({a for a in O1}).union({b for b in K1}))) - calc(K1)
#     return answ
