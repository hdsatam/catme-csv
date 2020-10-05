#!/usr/bin/python3

import numpy as np
import csv

def process_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        # gets names of features
        row1 = next(reader)
        for row in reader:
            if row[4] == '':
                continue
            if ',' in row[4]:
                continue
            if '.' in row[4]:
                continue
            if int(row[4]) >= 16 and int(row[4]) <= 24:
                print(row[2])
    
process_csv("catme.csv")