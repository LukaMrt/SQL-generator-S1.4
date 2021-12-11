class Participation:

    def __init__(self, student, study, duration):
        self.student = student
        self.study = study
        self.duration = duration

    def to_sql(self) -> str:
        return "INSERT INTO PARTICIPATION VALUES ({}, {}, {});" \
            .format(self.student, self.study, self.duration)
