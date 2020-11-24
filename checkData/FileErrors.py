import re
import model.Producer as pr
import model.Pharmacy as ph
import model.Contract as cr


def load_data(input_file):
    with open(input_file, "r") as file:
        line = file.readline()
        if line.lstrip()[0] != "#":
            raise ValueError(
                "Błąd w wersie 1. \"{} Poprawnie: \"# Producenci szczepionek (id | nazwa | dzienna produkcja)\"".format(
                    line))
        n = 1
        pr_ph_reg_ex = r"[ ]{0,}(\d+)+[ ]{0,}\|+[ ]{0,}([\w\-!@#$%^&*()+=.,<>\[\]\/{}\?\\'\";:~` ]+)\|+[ ]{0,}(\d+)"
        producers = []
        while True:
            line = file.readline()
            if re.match(pr_ph_reg_ex, line):
                idn = re.match(pr_ph_reg_ex, line).group(1)
                name = re.match(pr_ph_reg_ex, line).group(2)
                amount = re.match(pr_ph_reg_ex, line).group(3)
                producers.append(pr.Producer(idn, name, amount))
                n += 1
            else:
                break
        print("wczytano producentów")
        print(producers)
        print(n)
        if line.lstrip()[0] != "#":
            raise ValueError(
                "Błąd w wersie {} \"{} Poprawnie: \"# Apteki (id | nazwa | dzienne zapotrzebowanie)\"".format(n + 1,
                                                                                                              line))
        pharmacies = []
        while True:
            line = file.readline()
            if re.match(pr_ph_reg_ex, line):
                idn = re.match(pr_ph_reg_ex, line).group(1)
                name = re.match(pr_ph_reg_ex, line).group(2)
                amount = re.match(pr_ph_reg_ex, line).group(3)
                pharmacies.append(ph.Pharmacy(idn, name, amount))
                n += 1
            else:
                break
        print("wczytano apteki")
        print(pharmacies)
        print(n)
        if line.lstrip()[0] != "#":
            raise ValueError("Błąd w wersie {} \"{} Poprawnie: \"# Apteki (id | nazwa | dzienne zapotrzebowanie)\"".format(n + 1,
                                                                                                                 line))
        cr_reg_ex = r"[ ]*(\d+)+[ ]{0,}\|+[ ]*(\d+)+[ ]*\|[ ]*(\d+)+[ ]*\|+[ ]*(\d+.{0,1}\d{1,2})[ ]*"
        contracts = []
        while True:
            line = file.readline()
            if re.match(cr_reg_ex, line):
                id_pr = re.match(cr_reg_ex, line).group(1)
                id_ph = re.match(cr_reg_ex, line).group(2)
                amount = re.match(cr_reg_ex, line).group(3)
                price = re.match(cr_reg_ex, line).group(4)
                contracts.append(cr.Contract(id_pr, id_ph, amount, price))
                n += 1
            else:
                break
        print("wczytano producentów")
        print(contracts)




