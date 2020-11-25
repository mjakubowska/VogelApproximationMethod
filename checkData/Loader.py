import re
import model.Producer as pr
import model.Pharmacy as ph
import model.Contract as cr


class Loader:
    def __init__(self):
        self.producers = []
        self.pharmacies = []
        self.contracts = []

    def load_data(self, input_file):
        with open(input_file, "r") as file:
            line = file.readline().rstrip()
            while line == '':
                line = file.readline().rstrip()
                continue
            # line = file.readline()
            if line.lstrip()[0] != "#":
                raise ValueError(
                    "Błąd w wersie 1. \"{} Poprawnie: \"# Producenci szczepionek (id | nazwa | dzienna produkcja)\"".format(
                        line))
            n = 1
            pr_ph_reg_ex = r"[ ]{0,}(\d+)+[ ]{0,}\|+[ ]{0,}(\w+[\w\-!@#$%^&*()+=.,<>\[\]\/{}\?\\'\";:~` ]+)\|+[ ]{0,}(\d+)"
            index_pr = -1
            while True:
                line = file.readline().rstrip()
                if re.match(pr_ph_reg_ex, line):
                    idn = int(re.match(pr_ph_reg_ex, line).group(1))
                    print(idn)
                    if idn - index_pr != 1:
                        raise ValueError("Niepoprawny index producenta")
                    index_pr = idn
                    name = re.match(pr_ph_reg_ex, line).group(2)
                    amount = re.match(pr_ph_reg_ex, line).group(3)
                    self.producers.append(pr.Producer(idn, name, amount))
                    n += 1
                else:
                    break
            print("wczytano producentów")
            # print(self.producers)
            # print(n)
            while line == '':
                line = file.readline().rstrip()
                continue
            if line.lstrip()[0] != "#":
                raise ValueError(
                    "Błąd w wersie {} \"{} Poprawnie: \"# Apteki (id | nazwa | dzienne zapotrzebowanie)\"".format(n + 1,
                                                                                                                  line))
            index_ph = -1
            while True:
                line = file.readline()
                if re.match(pr_ph_reg_ex, line):
                    idn = int(re.match(pr_ph_reg_ex, line).group(1))
                    if idn - index_ph != 1:
                        raise ValueError("Niepoprawny index apteki")
                    index_ph = idn
                    name = re.match(pr_ph_reg_ex, line).group(2)
                    amount = re.match(pr_ph_reg_ex, line).group(3)
                    self.pharmacies.append(ph.Pharmacy(idn, name, amount))
                    n += 1
                else:
                    break
            print("wczytano apteki")
            # print(self.pharmacies)
            # print(n)
            line = line.rstrip()
            while line == '':
                line = file.readline().rstrip()
                continue
            if line.lstrip()[0] != "#":
                raise ValueError(
                    "Błąd w wersie {} \"{} Poprawnie: \"# Umowy ... (id | nazwa | dzienne zapotrzebowanie)\"".format(n + 1,
                                                                                                                  line))
            cr_reg_ex = r"[ ]*(\d+)+[ ]{0,}\|+[ ]*(\d+)+[ ]*\|[ ]*(\d+)+[ ]*\|+[ ]*(\d+.{0,1}\d{1,2})[ ]*"
            index_pr = -1
            index_ph = -1
            producers_contracts = []
            while True: # DODAĆ PRZYPADEK KIEDY JEST ENTERRRR!!!
                line = file.readline().rstrip()
                if re.match(cr_reg_ex, line):
                    id_pr = int(re.match(cr_reg_ex, line).group(1))
                    id_ph = int(re.match(cr_reg_ex, line).group(2))
                    amount = re.match(cr_reg_ex, line).group(3)
                    price = re.match(cr_reg_ex, line).group(4)
                    if id_pr == index_pr:
                        if id_ph - index_ph != 1:
                            #print(self.contracts)
                            raise ValueError("Bad index 1")
                        index_ph = id_ph
                        producers_contracts.append(cr.Contract(id_pr, id_ph, amount, price))
                    elif id_pr - index_pr == 1:
                        index_ph = 0
                        if id_ph - index_ph != 0:
                            raise ValueError("Bad index 3")
                        index_pr = id_pr
                        producers_contracts = [cr.Contract(id_pr, id_ph, amount, price)]
                        if id_ph  == 0:
                            self.contracts.append(producers_contracts)
                    else:
                        raise ValueError("Bad index 4")
                    n += 1
                else:
                    break
            if id_pr < len(self.producers) - 1:
                raise ValueError("Za mało producentów w umowach")
            if index_pr > len(self.producers) - 1:
                raise ValueError("Za dużo producentów w umowach")

            print("wczytano umowy")
            # print(self.contracts)
