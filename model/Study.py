from random import randint

from model.Date import Date


class Study:

    def __init__(self, id, name, date, duration, company_price, student_price, detention):
        self.id = id
        self.name = name
        date = date.split("/")
        self.date = Date(int(date[0]), int(date[1]), 2022 - randint(0, 5))
        self.duration = duration
        self.company_price = company_price
        self.student_price = student_price
        self.detention = detention
        self.in_charge = -1
        self.company = -1

    def to_sql(self) -> str:
        return "INSERT INTO ETUDE (NUMERO_ETUDIANT_RESPONSABLE, NUMERO_ENTREPRISE, NOM_ETUDE, DATE_CONVENTION," \
               "DUREE_ETUDE, RETENUE, PRIX_JOURNALIER_ENTREPRISE, PRIX_JOURNALIER_ETUDIANT) " \
               "VALUES ({}, {}, '{}', {}, {}, {}, {}, {});" \
            .format(self.in_charge, self.company, self.name, self.date.to_sql(), self.duration, self.detention,
                    self.company_price, self.student_price)
