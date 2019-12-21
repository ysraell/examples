
from __future__ import annotations
from typing import List, Callable, TypeVar, Tuple
from functools import reduce
from layer import Layer
from util import sigmoid, derivative_sigmoid
T = TypeVar('T')

class Network:
    def __init__(self, layer_structure: List[int], learning_rate: float,
                activate_function = sigmoid, 
                derivative_activate_function = derivative_sigmoid):
        if len(layer_structure) < 3:
            raise ValueError("Error: Should be at least 3 layers (1 input, 1 hidden, 1 output)")
        self.layers: List[Layer] = []
        input_layer = Layer(None, layer_structure[0], learning_rate, activate_function,
                           derivative_activate_function)
        self.layers.append(input_layer)
        self.sum_diff = None
        for previous, num_neurons in enumerate(layer_structure[1::]):
            next_layer = Layer(self.layers[previous], num_neurons, learning_rate, 
                               activate_function, derivative_activate_function)
            self.layers.append(next_layer)
        
    def outputs(self, input_: List[float]) -> List[float]:
        return reduce(lambda inputs, layer: layer.outputs(inputs), self.layers, input_)

    def backpropagate(self, expected: List[float]):
        last_layer = len(self.layers)-1
        self.layers[last_layer].calculate_deltas_for_output_layer(expected)
        for l in range(last_layer-1, 0, -1):
            self.layers[l].calulate_deltas_for_hidden_layer(self.layers[l+1])

    def update_weights(self):
        diff_list = []
        for layer in self.layers[1:]:
            for neuron in layer.neurons:
                for w in range(len(neuron.weights)):
                    diff = neuron.learning_rate*layer.previous_layer.output_cache[w]*neuron.delta
                    neuron.weights[w] = neuron.weights[w] + diff
                    diff_list.append(abs(diff))
        self.sum_diff = sum(diff_list)

    def train(self, inputs: List[List[float]], expecteds: List[List[float]]):
        for location, xs in enumerate(inputs):
            ys = expecteds[location]
            outs = self.outputs(xs)
            self.backpropagate(ys)
            self.update_weights()

    def validate(self, inputs: List[List[float]], expecteds: List[List[float]],
                interpret_output: Callable[[float], T]) -> Tuple[int, int, float]:
        correct = 0
        for input_, expected in zip(inputs, expecteds):
            result: T = interpret_output(self.outputs(input_))
            if result == expected:
                correct += 1
        percentagem = correct / len(inputs)
        return correct, len(inputs), percentagem
