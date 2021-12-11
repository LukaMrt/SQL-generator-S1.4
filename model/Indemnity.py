from model.Date import Date


class Indemnity:
    id = 0

    def __init__(self, study, student, date):
        self.id = Indemnity.id
        Indemnity.id += 1
        self.study = study
        self.student = student
        self.date = Date(date.day, date.month, date.year)

    def to_sql(self) -> str:
        return "INSERT INTO INDEMNITE VALUES ({}, {}, {}, {});" \
            .format(self.id, self.study, self.student, self.date.to_sql())
