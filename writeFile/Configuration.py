import codecs


class Configuration:
    def __init__(self):
        self.deals = []
        self.cost = 0

    def __repr__(self):
        string = ''
        for deal in self.deals:
            string += str(deal) + '\n'
        string += 'Koszt całkowity: ' + str(round(self.cost,2))
        return string

    def write_to_file(self, file_name):
        text_file = codecs.open(file_name, "w", "utf-8")
        text_file.write(self.__repr__())
        print(f"Wynik zapisano do pliku {file_name}")
        text_file.close()
