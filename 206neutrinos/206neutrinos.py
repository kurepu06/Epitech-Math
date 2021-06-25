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

number_value = -1
oldart_mean = -1
art_mean = -1
harm_mean = -1
std_deviation = -1
root_mean = -1

nxt_value = ""
new_value = -1

def compute_devitation():
    # sqrt(((regnestykkeFirkantet + pow(malinder, 2)) / n) - pow(a, 2)) * 1.0
    res = (((pow(std_deviation, 2) + pow(oldart_mean, 2)) * number_value) + pow(new_value, 2)) / (number_value + 1)
    res = math.sqrt(res - pow(art_mean, 2) * 1.00)
    return res

def compute_artMean():
    res = ((art_mean * number_value) + new_value) / (number_value + 1)
    return res

def compute_rootMean():
    res = (((pow(std_deviation, 2) + pow(art_mean, 2)) * number_value) + pow(new_value, 2)) / (number_value + 1)
    return math.sqrt(res)

def compute_harmMean():
    res = (number_value + 1) / (((1 / harm_mean) * number_value) + (1 / new_value))
    return res

def display_records_value():
    print('\tNumber of values:\t{:d}'.format(number_value))
    print('\tStandard deviation:\t{:0.2f}'.format(std_deviation))
    print('\tArithmetic mean:\t{:0.2f}'.format(art_mean))
    print('\tRoot mean square:\t{:0.2f}'.format(root_mean))
    print('\tHarmonic mean:\t\t{:0.2f}'.format(harm_mean))
    print()

lenarg = len(sys.argv)

if lenarg != 5:
    exit(84)

try :
    number_value = int(sys.argv[1])
    art_mean = float(sys.argv[2])
    harm_mean = float(sys.argv[3])
    std_deviation = float(sys.argv[4])
    
    if number_value < 0 or art_mean < 0 or harm_mean < 0 or std_deviation < 0:
        exit(84)
        
except ValueError:
    sys.exit(84)

while nxt_value != "END":
    nxt_value = input("Enter next value: ")
    try :
        new_value = int(nxt_value)
    except ValueError:
        continue
    oldart_mean = art_mean
    root_mean = compute_rootMean()
    art_mean = compute_artMean()
    std_deviation = compute_devitation()
    harm_mean = compute_harmMean()

    number_value += 1

    display_records_value()