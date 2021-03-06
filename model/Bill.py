from model.Date import Date


class Bill:

    def __init__(self, id, company, study, date):
        self.id = id
        self.company = company
        self.study = study
        self.date = Date(date.day, date.month, date.year)

    def to_sql(self):
        return "INSERT INTO FACTURE (NUMERO_ENTREPRISE, NUMERO_CONVENTION, DATE_FACTURE) VALUES ({}, {}, {});"\
            .format(self.company, self.study, self.date.to_sql())
