import numpy as np
from checkData.Loader import Loader


def find_2min_diff(min_list):
    min1 = 0
    min2 = 0
    for i in min_list:

    raise NotImplementedError()


class Vogl:
    def __init__(self, loader):
        self.matrix = []
        self.min_w = []
        self.min_k = []
        self.load_contracts(loader.contracts, len(loader.producers))

    def _load_contracts(self, contracts, rows):
        for pharmacies in range(rows):
            self.matrix.insert(pharmacies, contracts[pharmacies])

    def print_matrix(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def count_min_w(self):
        for i in range(len(self.matrix)):
            self.min_w.append(find_2min_diff(self.matrix[i]))



