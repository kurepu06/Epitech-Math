#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## intersection 
## File description:
## python code
##

import math
import os
import sys
import time

listSize = []
listCpy = []
listTheori = []
listTuple = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 13)]

khiX = [99, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 2, 1]

khiTable = [
    [0.00, 0.02, 0.06, 0.15, 0.27, 0.45, 0.71, 1.07, 1.64, 2.71, 3.84, 5.41, 6.63],
    [0.02, 0.21, 0.45, 0.71, 1.02, 1.39, 1.83, 2.41, 3.22, 4.61, 5.99, 7.82, 9.21],
    [0.11, 0.58, 1.01, 1.42, 1.87, 2.37, 2.95, 3.66, 4.64, 6.25, 7.81, 9.84, 11.34],
    [0.30, 1.06, 1.65, 2.19, 2.75, 3.36, 4.04, 4.88, 5.99, 7.78, 9.49, 11.67, 13.28],
    [0.55, 1.61, 2.34, 3.00, 3.66, 4.35, 5.13, 6.06, 7.29, 9.241, 1.07, 13.39, 15.09],
    [0.87, 2.20, 3.07, 3.83, 4.57, 5.35, 6.21, 7.23, 8.56, 10.64, 12.59, 15.03, 16.81],
    [1.24, 2.83, 3.82, 4.67, 5.49, 6.35, 7.28, 8.38, 9.80, 12.02, 14.07, 16.62, 18.48],
    [0.65, 3.49, 4.59, 5.53, 6.42, 7.34, 8.35, 9.52, 11.03, 13.36, 15.51, 18.17, 20.09],
    [2.09, 4.17, 5.38, 6.39, 7.36, 8.34, 9.41, 10.66, 12.24, 14.68, 16.92, 19.68, 21.67],
    [2.56, 4.87, 6.18, 7.27, 8.30, 9.34, 10.47, 11.78, 13.44, 15.99, 18.31, 21.16, 23.21],
]

freedom = 0
khi2 = 0

def probabilityDefective():
    res = 0
    defective = 0
    for pieceNbr in listSize:
        res += defective * pieceNbr
        defective += 1
    res /= 100 ## nombre moyen de piece defectueuse
    res /= 100 ## probabilité
    return res


def loi_bino(rel, aparition, proba):
    n = float(rel)
    k = float(aparition)
    p = float(proba)
    q = float(1 - proba)
    res = float(rel)
    res *= float((math.factorial(n) / (math.factorial(k) * math.factorial(n - k))))
    res *= float(pow(p, k) * pow(q, n - k))

    return res

def fillTheorie(prob):
    theo = 0
    x = 0

    for i in range(0, len(listCpy)):

        for j in range(listTuple[i][0], listTuple[i][1] + 1):
            theo += loi_bino(100, x, prob)
            x += 1

        listTheori.append(theo)
        theo = 0

def calculX2():
    o = 0
    t = 0
    res = 0

    for i in range(0, len(listCpy)):
        o = listCpy[i][0]
        t = listTheori[i]
        res += (pow(o - t, 2)) / t

    return res

def compactClass():
    index = 0
    while index < len(listTuple):
        if index < len(listTuple) - 1 and listTuple[index][1] == listTuple[index + 1][0]:
            listTuple[index] = (listTuple[index][0], listTuple[index + 1][1])
            del listTuple[index + 1]
            continue
        index += 1

def makeClass():
    index = 0
    indexTuple = 0
    realIndex = 0

    for i in listCpy:
        while listCpy[index][0] < 10:
            if index != len(listCpy) - 1:
                tup = (-1, -1)
                if index > 0 and listCpy[index + 1][0] < listCpy[index - 1][0]:
                    listCpy[index + 1][0] += listCpy[index][0]
                    tup = (listCpy[index][1], listCpy[index + 1][1])
                elif index > 0:
                    listCpy[index - 1][0] += listCpy[index][0]
                    tup = (listCpy[index - 1][1], listCpy[index][1])
                else:
                    listCpy[index + 1][0] += listCpy[index][0]
                    tup = (listCpy[index][1], listCpy[index + 1][1])
                del listCpy[index]
                realIndex += 1
                listTuple[indexTuple] = tup
                indexTuple += 1
                continue
            else:
                break
        indexTuple += 1
        index += 1
    compactClass()

def printTable():
    index = 0
    print("  x\t|", end='')
    for classe in listTuple:
        if index >= len(listSize):
            break
        if (classe[1] == 13):
            print(' {:d}+\t|'.format(classe[0]), end='')
            break
        if classe[0] != classe[1]:
            print(' {:d}-{:d}\t|'.format(classe[0], classe[1]), end='')
        else:
            print(' {:d}\t|'.format(classe[0]), end='')

        index +=1
    print(" Total")

    print("  Ox\t|", end='')
    for Ox in listCpy:
        print(' {:d}\t|'.format(Ox[0]), end='')
    print(" 100")

    print("  Tx\t|", end='')
    for Tx in listTheori:
        print(' {:0.1f}\t|'.format(round(Tx, 1)), end='')
    print(" 100")

def FreedomCalcul():
    res = len(listCpy) - 2

    return res

def printFitValidity():
    intervale = [0, 0]
    x = 0
    for i in khiTable[freedom - 1]:
        if i > khi2:
            intervale[1] = i
            if x > 0:
                intervale[0] = khiTable[freedom - 1][x - 1]
            break
        x += 1

    print("Fit validity:\t\t", end='')
    if intervale[0] != 0 and intervale[1] != 0:
        print('{:d}% < P < {:d}%'.format(khiX[x], khiX[x - 1]))
    elif intervale[0] != 0 :
        print("P < 1%")
    else:
        print("P > 99%")

##---- function ---- ##

lenarg = len(sys.argv)

if lenarg != 10:
    exit(84)

try :
    index = 0
    for i in range(1, len(sys.argv)):
        if int(sys.argv[i]) < 0 :
            sys.exit(84)
        listSize.append(int(sys.argv[i]))
        listCpy.append([int(sys.argv[i]), index])
        index += 1

except ValueError:
    sys.exit(84)

prob = probabilityDefective()
makeClass()
# print(listTuple)
fillTheorie(prob)
# print(listSize)
# print(prob)
# print(listTheori)
freedom = FreedomCalcul()
khi2 = calculX2()
printTable()
print('Distribution:\t\tB(100, {:0.4f})'.format(prob))
print('Chi-squared:\t\t{:0.3f}'.format(khi2))
print('Degrees of freedom:\t{:d}'.format(freedom))
printFitValidity()
