from operator import attrgetter
from checkData.Loader import Loader
from model.Deal import Deal


def find_2min_diff(min_list):
    min1 = min(min_list[0].price, min_list[1].price)
    min2 = max(min_list[0].price, min_list[1].price)
    for x in min_list[2::]:
        if x.price <= min1:
            min1, min2 = x.price, min1
        elif x.price < min2:
            min2 = x.price
    return round(min2 - min1, 2)


class Vogl:
    def __init__(self, loader):
        self.matrix = []
        self.min_r = []
        self.min_c = []
        self.loader = loader
        self.solution = []
        self._load_contracts(loader.contracts, len(loader.producers))

    def _load_contracts(self, contracts, rows):
        for pharmacies in range(rows):
            self.matrix.insert(pharmacies, contracts[pharmacies])
        self._find_mins()
        self.find_max_mins()

    def print_matrix(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def _find_mins(self):
        for rows in self.matrix:
            self.min_r.append(find_2min_diff(rows))
        for columns in range(len(self.matrix[0])):
            column = []
            for rows in range(len(self.matrix)):
                column.append(self.matrix[rows][columns])
            self.min_c.append(find_2min_diff(column))
        print(f"min_r: {self.min_r}, min_c: {self.min_c}")

    def find_max_mins(self):
        value_c = max(self.min_c) #max
        value_r = max(self.min_r) #max
        if value_c > value_r: # >
            index_c = self.min_c.index(value_c)
            index_r = self.matrix.index(min(self.matrix, key=lambda x: x[index_c].price))
        else: # value_r >= value_c
            index_r = self.min_r.index(value_r)
            index_c = self.matrix[index_r].index(min(self.matrix[index_r], key=attrgetter('price')))
        return index_r, index_c #row-dostawca, #column-apteka

    def add_to_solution(self):
        index_r, index_c = self.find_max_mins()
        contract = self.matrix[index_r][index_c]
        id_pr = self.matrix[index_r][index_c].id_pr
        id_ph = self.matrix[index_r][index_c].id_ph
        producer = self.loader.producers[id_pr]
        pharmacy = self.loader.pharmacies[id_ph]
        if pharmacy.amount > contract.amount:
            deal = Deal(producer, pharmacy, contract.amount, contract.price)
            self.solution.append(deal)
            self.loader.producers[id_pr].amount -= contract.amount
            self.loader.pharmacies[id_ph].amount -= contract.amount
        print("solution: ", self.solution)
        print("pharma: ", pharmacy)
        print("producer: ", producer)

