class Contract:

    def __init__(self, id_pr, id_ph, amount, price):
        self.id_pr = id_pr
        self.id_ph = id_ph
        self.amount = amount
        self.price = price

    def __repr__(self):
        return f'{self.id_pr} | {self.id_ph} | {self.amount} | {self.price}'

    def __eq__(self, other):
        if isinstance(other, Contract):
            if self.id_pr == other.id_pr and self.id_ph == other.id_ph:
                if self.amount == other.amount and self.price == other.price:
                    return True
        return False
