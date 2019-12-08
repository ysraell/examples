
from __future__ import annotations
from typing import Lista, Callable, Optional
from random import random
from neuron import Neuron
from util import dot_prod

class Layer:
    def __init__(self, previous_layer: Optional[Layer], num_neurons: int,
                learning_rate: float, activation_function: Callable[[float], float],
                derivative_activation_function: Callable[[float], float]):
        self.previous_layer = previous_layer
        self.neurons: List[Neuron] = []
        for i in range(num_neurons):
            if previous_layer is None:
                random_weights = []
            else:
                random_weights = [random() for _ in range(len(previous_layer.neurons))]
            neuron = Neuron(random_weights, learning_rate, activation_function,
                           derivative_activation_function)
            self.neurons.append(neuron)
        self.output_cache = [0.0 for _ in range(num_neurons)]

    def outputs(self, inputs: List[float]) -> List[float]:
        if self.previous_layer is None:
            self.output_cache = inputs
        else:
            self.output_cache = [n.output(inputs) for n in self.neurons]
        return self.output_cache
    
    def calculate_deltas_for_output_layer(self, expected: List[float]):
        for n in range(len(self.neurons)):
            tmp = self.neurons[n].output_cache * (expected[n] - self.output_cache[n])
            self.neurons[n].delta = self.neurons[n].derivative_activation_function(tmp)
            
    def calulate_deltas_for_hidden_layer(self, next_layer):
        for index, neuron in enumerate(self.neurons):
            next_weights = [n.weights[index] for n in next_layer.neurons]
            next_deltas = [n.delta for n in next_layer.neurons]
            sum_weights_and_deltas = dot_prod(next_weights, next_deltas)
            neuron.delta = neuron.derivative_activation_function(neuron.output_cache)*sum_weights_and_deltas
            
