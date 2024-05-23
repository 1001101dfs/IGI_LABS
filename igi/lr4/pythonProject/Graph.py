from collections import Counter
import math


class Graph:

    def __init__(self):
        self.elements = []

    def add_element(self, x):
        self.elements.append(x)

    def mode(self):
        freq_counter = Counter(self.elements)
        max_freq = max(freq_counter.values())
        mode_values = [key for key, value in freq_counter.items() if value == max_freq]
        return mode_values

    def median(self):
        sorted_sequence = sorted(self.elements)
        length = len(sorted_sequence)
        mid = length // 2

        if length % 2 == 0:
            return (sorted_sequence[mid - 1] + sorted_sequence[mid]) / 2
        else:
            return sorted_sequence[mid]

    def sred_znach(self):
        return sum(self.elements) / len(self.elements)

    def variance(self):
        mean = sum(self.elements) / len(self.elements)
        squared_diff = [(x - mean) ** 2 for x in self.elements]
        variance_value = sum(squared_diff) / len(self.elements)
        return variance_value

    def standard_deviation(self):
        mean = sum(self.elements) / len(self.elements)
        squared_diff = [(x - mean) ** 2 for x in self.elements]
        variance_value = sum(squared_diff) / len(self.elements)
        standard_deviation_value = math.sqrt(variance_value)
        return standard_deviation_value
