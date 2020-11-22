import re
import model.Producer as pr


def check_syntax(input_file):
    with open(input_file, "r") as file:
        line = file.readline()
        if line[0] != "# Producenci szczepionek (id | nazwa | dzienna produkcja)\n":
            print(
                "Błąd w wersie 1. \"{} Poprawnie: \"# Producenci szczepionek (id | nazwa | dzienna produkcja)\"".format(
                    line))
        n = 1
        places_reg_ex = r"[ ]{0,}(\d)+[ ]{0,}\|+[ ]{0,}([\w\-!@#$%^&*()+=.,<>\[\]\/{}\?\\'\";:~` ]+)\|+[ ]{0,}(\d+)"
        producers = list()
        while True:
            line = file.readline()
            if re.match(places_reg_ex, line):
                idn = re.match(places_reg_ex, line).group(1)
                name = re.match(places_reg_ex, line).group(2)
                amount = re.match(places_reg_ex, line).group(3)
                producers.append(pr.Producer(idn, name, amount))
                n += 1
            else:
                break
        print("wczytano producentów")
        print(n)
        if line != "# Apteki (id | nazwa | dzienne zapotrzebowanie)\n":
            print(
                "Błąd w wersie {} \"{} Poprawnie: \"# Apteki (id | nazwa | dzienne zapotrzebowanie)\"".format(n + 1,
                                                                                                              line))
        pharmacies = []
        while True:
            line = file.readline()
            if re.match(places_reg_ex, line):
                idn = re.match(places_reg_ex, line).group(1)
                name = re.match(places_reg_ex, line).group(2)
                amount = re.match(places_reg_ex, line).group(3)
                pharmacies.append(pr.Pharmacy(idn, name, amount))
                n += 1
            else:
                break
        print("wczytano apteki")
        print(n)
        if line != "# Apteki (id | nazwa | dzienne zapotrzebowanie)\n":
            print(
                "Błąd w wersie {} \"{} Poprawnie: \"# Apteki (id | nazwa | dzienne zapotrzebowanie)\"".format(n + 1,
                                                                                                              line))
