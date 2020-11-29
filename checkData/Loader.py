import re
import sys
import model.Producer as pr
import model.Pharmacy as ph
import model.Contract as cr


class Loader:
    def __init__(self, name):
        self.name = name
        self.producers = []
        self.pharmacies = []
        self.contracts = []

    def load_data(self, file):
        n = 1
        line = file.readline().rstrip()
        try:
            if line.lstrip()[0] != "#":
                raise ValueError(
                    f"Błąd w wersie {n} \"{line}\"\n"
                    f"Nagłowek powinien zaczynać się od znaku \"#\"\n"
                    f"Np. \"# Producenci szczepionek (id | nazwa | dzienna produkcja)\"")
        except IndexError:
            print("plik jest pusty")
            sys.exit(1)
        pr_ph_reg_ex = r"[ ]{0,}(\d+)+[ ]{0,}\|+[ ]{0,}(\w+[\w\-!@#$%^&*()+=.,<>\[\]\/{}\?\\'\";:~` ]+)\|+[ ]{0,}(\d+)"
        index_pr = -1
        while True:
            line = file.readline().rstrip()
            n += 1
            if re.match(pr_ph_reg_ex, line):
                idn = int(re.match(pr_ph_reg_ex, line).group(1))
                if idn - index_pr != 1:
                    raise ValueError(f"Błąd w wersie {n}: \"{line}\"\n Niepoprawny index producenta")
                index_pr = idn
                name = re.match(pr_ph_reg_ex, line).group(2)
                amount = int(re.match(pr_ph_reg_ex, line).group(3))
                self.producers.append(pr.Producer(idn, name, amount))
            else:
                break
        # print("wczytano producentów")
        if line.lstrip()[0] != "#":
            raise ValueError(
                f"Błąd w wersie {n}, błędne dane producenta lub zły nagłówek: \"{line}\"\n"
                f"Poptawna forma danych producenta: id | nazwa | dzienna produkcja\n"
                f"Poprawny nagłówek powinien zaczynać się od znaku \"#\"")
        index_ph = -1
        while True:
            line = file.readline()
            n += 1
            if re.match(pr_ph_reg_ex, line):
                idn = int(re.match(pr_ph_reg_ex, line).group(1))
                if idn - index_ph != 1:
                    raise ValueError(f"Błąd w wersie {n}: \"{line}\" Niepoprawny index apteki")
                index_ph = idn
                name = re.match(pr_ph_reg_ex, line).group(2)
                amount = int(re.match(pr_ph_reg_ex, line).group(3))
                self.pharmacies.append(ph.Pharmacy(idn, name, amount))
            else:
                break
        # print("wczytano apteki")
        line = line.rstrip()
        if line.lstrip()[0] != "#":
            raise ValueError(
                 f"Błąd w wersie {n}, błędne dane apteki lub zły nagłówek: \"{line}\"\n"
                 f"Poptawna forma danych apteki: id | nazwa | dzienne zapotrzebowanie\n"
                 f"Poprawny nagłówek powinien zaczynać się od znaku \"#\"")
        cr_reg_ex = r"[ ]*(\d+)+[ ]{0,}\|+[ ]*(\d+)+[ ]*\|[ ]*(\d+)+[ ]*\|+[ ]*(\d+.{0,1}\d{1,2})[ ]*"
        index_pr = -1
        index_ph = -1
        while True:
            line = file.readline().rstrip()
            n += 1
            if re.match(cr_reg_ex, line):
                id_pr = int(re.match(cr_reg_ex, line).group(1))
                id_ph = int(re.match(cr_reg_ex, line).group(2))
                amount = int(re.match(cr_reg_ex, line).group(3))
                price = float(re.match(cr_reg_ex, line).group(4))
                if id_pr == index_pr:
                    if id_ph - index_ph != 1:
                        raise ValueError(f"Zły index apteki w wersie {n}: \"{line}\"\n"
                                         f"Indexy aptek dla danego producenta muszą być kolejnymi liczbami naturalnymi"
                                         f"zaczynając od 0 ")
                    index_ph = id_ph
                    if id_pr == 0:
                        self.contracts.append([])
                        self.contracts[id_ph].append(cr.Contract(id_pr, id_ph, amount, price))
                    else:
                        self.contracts[id_ph].append(cr.Contract(id_pr, id_ph, amount, price))
                elif id_pr - index_pr == 1:
                    index_ph = 0
                    if id_ph - index_ph != 0:
                        raise ValueError(f"Zły index apteki lub producenta w wersie {n}: \"{line}\"\n"
                                         f"Indexy aptek dla danego producenta muszą być kolejnymi liczbami naturalnymi"
                                         f"zaczynając od 0 ")
                    index_pr = id_pr
                    if id_pr == 0:
                        self.contracts.append([])
                        self.contracts[0].append(cr.Contract(id_pr, id_ph, amount, price))
                    else:
                        self.contracts[id_ph].append(cr.Contract(id_pr, id_ph, amount, price))
                else:
                    raise ValueError(f"Zły index producenta w wersie {n}: \"{line}\"\n")
            else:
                break
        if id_pr < len(self.producers) - 1:
            raise ValueError(f"Brakuje umów producenta o id {len(self.producers) - 1}")
        if index_pr > len(self.producers) - 1:
            raise ValueError("Za dużo producentów w umowach")
        # print("wczytano umowy")
        print(f"wczytano dane z pliku {file.name}")

    def set_pharmacies(self, ph_list):
        self.pharmacies = ph_list

    def set_producers(self, pr_list):
        self.producers = pr_list

    def set_contracts(self, cr_list):
        self.contracts
