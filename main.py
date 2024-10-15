"""This file is a draft. It will look at data.csv file
and output the error, coefficients for the given polynomial
and will stop early if max_error is successfully under."""
from itertools import product
import math
import numpy as np
import os
import random


def get_all_data():
    filenames = [x for x in os.listdir("./") if x[:4] == "data"]
    files = []
    for filename in filenames:
        lines = open(filename, "r").read().split("\n")
        lines.pop()
        lines.pop()
        lines = [line.split(",") for line in lines]
        [line.pop(0) for line in lines]
        files.append([[float(elem) for elem in line] for line in lines])
    return files


def produce_all_combinations(max_complexity):
    for iteration in range(2, max_complexity+2):
        copy = variables[:len(lines[0])-1]
        for itera in range(2, iteration):
            copy += [''.join(p) for p in product(variables[:len(lines[0])-1], repeat=itera)]
        yield(copy)


def calc_coefs(comb):
    matrix = []
    for line_index in range(len(lines)):
        col = []
        for index in range(len(comb)):
            amount = 1
            for letter in comb[index]:
                amount *= lines[line_index][variables.index(letter)]
            col.append(amount)
        matrix.append(col)

    for line_index in range(len(lines)):
        matrix[line_index].append(1)

    X = np.asarray([np.asarray(i) for i in matrix])
    y = np.asarray([l[-1] for l in lines])
    
    XtX = np.dot(X.T, X)
    Xty = np.dot(X.T, y)
    XtX_inv = np.linalg.inv(XtX)
    beta_hat = np.dot(XtX_inv, Xty)
    residuals = y - np.dot(X, beta_hat)
    return (sum([r**2 for r in residuals])/residuals.shape[0], comb, beta_hat)


def consolidate_expr(expr):
    holder = {}
    for k in expr:
        k = [a for a in k]
        k.sort()
        k = ''.join(k)
        if not (k in holder):
            holder[k] = 1
        else:
            holder[k] += 1
    return list(holder.keys())


variables = list('abcdefghijklmnopqrstuvwxyz')
lines = open("data.csv", "r").read().split("\n")
lines.pop()
X = [l.split(',') for l in lines]
lines = [[float(x) for x in l] for l in X]
del X

# lines = [[float(line.split(",")[0]), float(line.split(",")[1])] for line in lines]
print(len(lines), 'lines of data')


max_error = 0.1
output = []
for expr in produce_all_combinations(5):
    expr = consolidate_expr(expr)
    coefs = calc_coefs(expr)
    output.append(coefs)
    print(coefs)
    if coefs[0] < max_error:
        print("we did it")
        break


output.sort(reverse=True)
print(output)
