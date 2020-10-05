#!/usr/bin/python3

import numpy as g
import csv as e

def h(a):
    with open(a) as f:
        b = e.reader(f, delimiter=',')
        # gets names of features
        c = next(b)
        for d in b:
            if d[4] == '':
                continue
            if ',' in d[4]:
                continue
            if '.' in d[4]:
                continue
            if int(d[4]) >= 16 and int(d[4]) <= 24:
                print(d[2])
    
h("catme.csv")
