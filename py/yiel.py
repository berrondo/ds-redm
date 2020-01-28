from finais import *
for k, v in finais.items():
    s = finais_cfd[k] - v
    print(len(v), len(finais_cfd[k]), len(s), k, s)
    # 5225 5296 73 Demanda sem ônus em pontos de função concluída {5379, 901, 519, 4744, 3340, 5260, 3598, 1040, 2320, 3090, 4368, 1812, 3863, 2077, 4126, 4662, 2722, 2723, 2851, 38, 1830, 4137, 2859, 2093, 1838, 1714, 1842, 3891, 4020, 822, 951, 2744, 1081, 4153, 2875, 2876, 3261, 830, 959, 832, 831, 2878, 2882, 3394, 1093, 3141, 1735, 3395, 1354, 203, 3148, 4557, 4943, 1488, 4926, 1622, 4311, 1880, 4184, 4573, 2270, 2912, 3040, 2018, 2402, 1892, 4064, 2665, 3051, 2670, 4079, 6713, 4721}
    # 2920 2997 77 Demanda com ônus em pontos de função concluída {768, 1793, 2436, 261, 1669, 1545, 522, 1294, 4879, 2577, 1556, 1559, 1052, 1820, 2204, 417, 802, 1697, 5281, 1573, 423, 2599, 3879, 1579, 812, 2248, 1971, 2249, 1205, 1845, 1335, 2611, 2740, 1598, 1601, 2881, 325, 1606, 8391, 839, 841, 969, 1223, 2124, 1485, 1997, 207, 208, 1745, 722, 4300, 6740, 7765, 215, 1623, 345, 5335, 991, 483, 1123, 744, 618, 236, 1004, 878, 495, 1644, 241, 881, 8435, 1523, 3052, 4597, 7795, 1529, 1018, 2814}
    # 877 908 31 Demanda cancelada {8447, 390, 267, 268, 4372, 3093, 7829, 895, 3864, 7965, 1568, 1964, 819, 3123, 6198, 8375, 2874, 4542, 4543, 4927, 958, 8390, 1607, 2901, 2782, 5606, 4583, 4848, 2551, 888, 767}

# from csv import DictReader
#
# DEMANDAS = {}
# FINAIS = {}
#
#
# with open('demanda_finalizadas.csv', newline='', encoding="utf8") as f:
#     reader = DictReader(f)
#     for row in reader:
#         demanda = int(row['demanda'])
#         status = row['para'] or "SEM_DESTINO"
#
#         DEMANDAS[demanda] = status
#
# for d, s in DEMANDAS.items():
#     FINAIS[s] = FINAIS.get(s, []) + [d]
#
# for k, v in FINAIS.items():
#     FINAIS[k] = set(v)
#
# with open('finais.txt', 'w') as o:
#     print(FINAIS, file=o)



# from time import sleep
#
# def oscila(i=0):
#     while True:
#         i += 1
#         yield i
#         yield i * -1
#
# osc = oscila()
# print(osc.__next__())
# print(osc.__next__())
# print(osc.__next__())
# print(osc.__next__())
# print(osc.__next__())
# print(osc.__next__())
# print()
# osc = oscila(173)
# print(osc.__next__())
# print(osc.__next__())
# print(osc.__next__())
# print(osc.__next__())
# print(osc.__next__())
# print(osc.__next__())
# print(osc.__next__())
# print(osc.__next__())
# print(osc.__next__())
#
# for x in oscila():
#     sleep(1)
#     print(x)