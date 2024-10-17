import pandas as pd
import pytest

def middleMark(filename, indexLine):
    fl = pd.read_csv(filename)
    sumOfTests = fl['Test1'][indexLine] + fl['Test2'][indexLine] + fl['Test3'][indexLine] + fl['Test4'][indexLine]
    return sumOfTests / 4

def returnFinal(indexLine):
    fl = pd.read_csv('grades.csv')
    return fl['Final'][indexLine]

def returnList():
    fl = pd.read_csv('grades.csv')
    out = []
    inside = []
    for line in range(fl.shape[0]):
        expected = middleMark('grades.csv', line)
        actual = fl['Final'][line]
        inside.append(expected)
        inside.append(actual)
        out.append(inside)
        inside = []
    print(out)
    return out

returnList()

