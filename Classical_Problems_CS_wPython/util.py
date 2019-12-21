
from typing import List
from math import exp

def dot_prod(xs: List[float], ys: List[float]) -> float:
    return sum(x*y for x,y in zip(xs,ys))

def sigmoid(x: float) -> float:
    return 1.0/(1.0 +exp(-x))

def derivative_sigmoid(x: float) -> float:
    sig = sigmoid(x)
    return sig*(1 - sig)

def normalize_by_feature_scaling(dataset: List[List[float]]) -> None:
    for col_num in range(len(dataset)):
        column = [row[col_num] for row in dataset]
        maximun = max(column)
        minimun = min(column)
        for row_num in range(len(dataset)):
            dataset[row_num][col_num] = (dataset[row_num][col_num]-minimun)/(maximun-minimun)
