from model.Date import Date


class Cost:

    def __init__(self, id, study, student, date, type, amount):
        self.id = id
        self.payment = None
        self.study = study
        self.student = student
        self.date = Date(date.day, date.month, date.year)
        self.type = type
        self.amount = amount

    def to_sql(self) -> str:
        return "INSERT INTO FRAIS" \
               " (NUMERO_REMBOURSEMENT_FRAIS, NUMERO_CONVENTION, NUMERO_ETUDIANT," \
               "DATE_FRAIS, TYPE_FRAIS, MONTANT_FRAIS) " \
               " VALUES ({}, {}, {}, {}, '{}', {});" \
            .format(self.payment if self.payment is not None else 'NULL', self.study, self.student, self.date.to_sql(),
                    self.type, self.amount)
