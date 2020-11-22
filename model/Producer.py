class Producer:

    def __init__(self, idn, name, amount):
        self.idn = idn
        self.name = name
        self.amount = amount

    def toString(self):
        return self.name

