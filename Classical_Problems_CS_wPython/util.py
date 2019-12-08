
from typing import List
from math import exp

def dot_prod(xs: List[float], ys: List[float]) -> float:
    return sum(x*y for x,y in zip(xs,ys))

def sigmoid(x: float) -> float:
    return 1.0/(1.0 +exp(-x))

def derivative_sigmoid(x: float) -> float:
    sig = sigmoid(x)
    return sig*(1 - sig)
