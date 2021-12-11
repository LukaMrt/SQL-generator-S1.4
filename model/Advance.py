class Advance:
    id = 0

    def __init__(self, student, study, amount):
        self.id = Advance.id
        Advance.id += 1
        self.student = student
        self.study = study
        self.amount = amount

    def to_sql(self) -> str:
        return "INSERT INTO ACOMPTE VALUES ({}, {}, {}, {});" \
            .format(self.id, self.student, self.study, self.amount)
