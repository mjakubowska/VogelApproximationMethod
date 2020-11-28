class Deal:
    def __init__(self, producer, pharmacy, amount, price):
        self.producer = producer
        self.pharmacy = pharmacy
        self.amount = amount
        self.price = price

    def __repr__(self):
        return f"{self.producer.name} -> {self.pharmacy.name} [Koszt = {self.amount} * {self.price} = {round(self.amount*self.price, 2)} zl] "

