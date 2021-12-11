from model.Date import Date


class Payment:
    id = 0

    def __init__(self, date):
        self.id = Payment.id
        Payment.id += 1
        self.date = Date(1, date.month, date.year)

    def to_sql(self) -> str:
        return "INSERT INTO REMBOURSEMENT_FRAIS VALUES ({}, {});" \
            .format(self.id, self.date.to_sql())
