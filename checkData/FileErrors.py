import re
import model.Producer as pr


def check_syntax(input_file):
    with open(input_file, "r") as file:
        line = file.readline()
        if line != "# Producenci szczepionek (id | nazwa | dzienna produkcja)\n":
            print(
                "Błąd w wersie 1. \"{} Poprawnie: \"# Producenci szczepionek (id | nazwa | dzienna produkcja)\"".format(
                    line))
            n = 1
        prodRegEx = r"[ ]{0,}(\d)+[ ]{0,}\|+[ ]{0,}([\w\-!@#$%^&*()+=.,<>\[\]\/{}\?\\'\";:~` ]+)\|+[ ]{0,}(\d+)"
        producers = list()
        for line in file.readlines():
            if re.match(prodRegEx, line):
                idn = re.match(prodRegEx, line).group(1)
                name = re.match(prodRegEx, line).group(2)
                amount = re.match(prodRegEx, line).group(3)
                producers.append(pr.Producer(idn, name, amount))
        print(producers[0].name)
