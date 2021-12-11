from model.Date import Date


class Cost:
    id = 0

    def __init__(self, study, student, date, type, amount):
        self.id = Cost.id
        Cost.id += 1
        self.payment = None
        self.study = study
        self.student = student
        self.date = Date(date.day, date.month, date.year)
        self.type = type
        self.amount = amount

    def to_sql(self) -> str:
        return "INSERT INTO FRAIS VALUES ({}, {}, {}, {}, {}, '{}', {});" \
            .format(self.id, self.payment if self.payment is not None else 'NULL', self.study, self.student, self.date.to_sql(),
                    self.type, self.amount)
