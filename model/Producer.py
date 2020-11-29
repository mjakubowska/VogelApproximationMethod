class Producer:

    def __init__(self, idn, name, amount):
        self.idn = idn
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f'{self.idn} | {self.name} | {self.amount}'

