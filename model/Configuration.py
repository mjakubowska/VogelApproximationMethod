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
