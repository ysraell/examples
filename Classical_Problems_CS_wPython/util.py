
from typing import List
from math import exp, copysign

sign = lambda x: copysign(1, x) 

def dot_prod(xs: List[float], ys: List[float]) -> float:
    return sum(x*y for x,y in zip(xs,ys))

def sigmoid(x: float) -> float:
    try:
        return 1.0/(1.0+exp(-x))
    except:
        return 1.0/(1.0+exp(-sign(x)*min(abs(x),500)))

def derivative_sigmoid(x: float) -> float:
    sig = sigmoid(x)
    return sig*(1 - sig)

def normalize_by_feature_scaling(dataset: List[List[float]]) -> None:
    for col_num in range(len(dataset[0])):
        column = [row[col_num] for row in dataset]
        maximun = max(column)
        minimun = min(column)
        for row_num in range(len(dataset)):
            dataset[row_num][col_num] = (dataset[row_num][col_num]-minimun)/(maximun-minimun)
