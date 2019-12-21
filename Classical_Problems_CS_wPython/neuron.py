
from typing import List, Callable
from util import dot_prod

class Neuron:
    def __init__(self, weights: List[float], learning_rate: float,
                 activation_function: Callable[[float], float],
                 derivative_activation_function: Callable[[float], float]):
        self.weights = weights
        self.activation_function = activation_function
        self.derivative_activation_function = derivative_activation_function
        self.learning_rate = learning_rate
        self.output_cache = 0.0
        self.delta = 0.0
        
    def output(self, inputs: List[float]) -> float:
        self.output_cache = dot_prod(inputs, self.weights)
        return self.activation_function(self.output_cache)
    
    
