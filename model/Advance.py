class Advance:

    def __init__(self, id, student, study, amount):
        self.id = id
        self.student = student
        self.study = study
        self.amount = amount

    def to_sql(self) -> str:
        return "INSERT INTO ACOMPTE (NUMERO_ETUDIANT, NUMERO_ETUDE, VALEUR_ACOMPTE) VALUES ({}, {}, {});" \
            .format(self.student, self.study, self.amount)
