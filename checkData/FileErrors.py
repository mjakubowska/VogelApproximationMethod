def check_syntax(input_file):
    with open(input_file, "r") as file:
        line = file.readline()
        if line != "# Producenci szczepionek (id | nazwa | dzienna produkcja))":
            print("Błąd w wersie 1. \"{} Poprawnie: \"# Producenci szczepionek (id | nazwa | dzienna produkcja))\"".format(line))

