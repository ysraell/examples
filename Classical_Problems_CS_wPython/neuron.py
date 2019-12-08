
from typing import List, Callable
from util import dot_prod

class Neuron:
    def __init__(self, weights: List[float], learning_rate: float,
                 activation_function: Callable[[float], float],
                 derivative_activation_function: Callable[[float], float]):
        self.weights = weights
