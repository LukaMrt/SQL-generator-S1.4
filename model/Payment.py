from model.Date import Date


class Payment:
    id = 0

    def __init__(self, date):
        self.id = Payment.id
        Payment.id += 1
        self.date = Date(date.day, date.month, date.year)

    def __str__(self):
        return "INSERT INTO REMBOURSEMENT_FRAIS VALUES ({}, {});" \
            .format(self.id, self.date)
