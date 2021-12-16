from model.Date import Date


class Payment:

    def __init__(self, id, date):
        self.id = id
        self.date = Date(1, date.month, date.year)

    def to_sql(self) -> str:
        return "INSERT INTO REMBOURSEMENT_FRAIS (DATE_REMBOURSEMENT_FRAIS) VALUES ({});" \
            .format(self.date.to_sql())
