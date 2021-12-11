from model.Date import Date


class Indemnity:

    def __init__(self, id, study, student, date):
        self.id = id
        self.study = study
        self.student = student
        self.date = Date(date.day, date.month, date.year)

    def to_sql(self) -> str:
        return "INSERT INTO INDEMNITES VALUES ({}, {}, {}, {});" \
            .format(self.id, self.study, self.student, self.date.to_sql())
