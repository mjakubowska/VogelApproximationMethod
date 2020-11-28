from operator import attrgetter
from checkData.Loader import Loader
from model.Deal import Deal
from model.Configuration import Configuration


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
        self.solution = Configuration()
        self._load_contracts(loader.contracts, len(loader.pharmacies))

    def _load_contracts(self, contracts, rows):
        for producers in range(rows):
            self.matrix.insert(producers, contracts[producers])
        self._find_mins()
        print(self.matrix)
        itr = 0
        while len(self.matrix) > 0:
            self.fill_pharmacy()
            itr += 1
        print(len(self.matrix))
        print(self.matrix)
        print(self.solution)

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

    def _update_mins(self):
        self.min_r = []
        for rows in self.matrix:
            self.min_r.append(find_2min_diff(rows))

    def find_max_mins(self):
        value_c = max(self.min_c)
        value_r = max(self.min_r)
        if value_c > value_r: # >
            index_c = self.min_c.index(value_c)
            index_r = self.matrix.index(min(self.matrix, key=lambda x: x[index_c].price))
        else: # value_r >= value_c
            index_r = self.min_r.index(value_r)
            index_c = self.matrix[index_r].index(min(self.matrix[index_r], key=attrgetter('price')))
        return index_r, index_c #, index_r #row-dostawca, #column-apteka

    def fill_pharmacy(self):
        index_r, index_c = self.find_max_mins()
        contract = self.matrix[index_r][index_c]
        id_pr = self.matrix[index_r][index_c].id_pr
        id_ph = self.matrix[index_r][index_c].id_ph
        pharmacy = self.loader.pharmacies[id_ph]
        while self.loader.pharmacies[id_ph] != 0:
            producer = self.loader.producers[id_pr]
            if pharmacy.amount <= producer.amount:
                if pharmacy.amount > contract.amount:
                    deal_amount = contract.amount
                else:
                    deal_amount = pharmacy.amount
                deal = Deal(producer, pharmacy, deal_amount, contract.price)
                self.solution.deals.append(deal)
                self.solution.cost += round(deal_amount * contract.price, 2)
                self.loader.producers[id_pr].amount -= deal_amount
                self.loader.pharmacies[id_ph].amount -= deal_amount
                self.matrix[index_r][index_c].amount -= deal_amount
                if self.matrix[index_r][index_c].amount == 0: #jesli kontrakt sie wyczerpal
                    del self.matrix[index_r][index_c]
                if self.loader.producers[id_pr].amount == 0:
                    for i in range(len(self.matrix)):
                        del self.matrix[i][index_c]
                    del self.min_c[index_c]
                    self._update_mins()
                if self.loader.pharmacies[id_ph].amount == 0:
                    del self.matrix[index_r]
                    del self.min_r[index_r]
                    # print(f"Hurra, wypelniono apteke {id_ph}!!!")
                    break
            elif pharmacy.amount > producer.amount:
                if producer.amount > contract.amount:
                    deal_amount = contract.amount
                else:
                    deal_amount = producer.amount
                deal = Deal(producer, pharmacy, deal_amount, contract.price)
                self.solution.deals.append(deal)
                self.solution.cost += round(deal_amount * contract.price, 2)
                self.loader.producers[id_pr].amount -= deal_amount
                self.loader.pharmacies[id_ph].amount -= deal_amount
                self.matrix[index_r][index_c].amount -= deal_amount
                if self.matrix[index_r][index_c].amount == 0:
                    del self.matrix[index_r][index_c]
                if producer.amount == 0:
                    for i in range(len(self.matrix)):
                        del self.matrix[i][index_c]
                    del self.min_c[index_c]
                    self._update_mins()
            if len(self.matrix[index_r]) == 0:
                print(f"Nie udało się zapełcić apteki {id_ph}")
                break
            index_c = self.matrix[index_r].index(min(self.matrix[index_r], key=attrgetter('price')))
            contract = self.matrix[index_r][index_c]
            id_pr = self.matrix[index_r][index_c].id_pr
