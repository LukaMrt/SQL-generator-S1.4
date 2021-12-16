from random import randint

from model.Date import Date


class Student:

    def __init__(self, id, name, birth, address, social_number):
        self.id = id
        self.name = name
        date = birth.split("/")
        self.birth = Date(int(date[0]), int(date[1]), 2003 - randint(0, 10))
        self.address = address
        self.social_number = social_number

    def to_sql(self) -> str:
        return "INSERT INTO ETUDIANT" \
               " (NOM_ETUDIANT, DATE_NAISSANCE_ETUDIANT, ADRESSE_ETUDIANT, NUMERO_SECURITE_SOCIALE) " \
               "VALUES ('{}', {}, '{}', '{}');" \
            .format(self.name, self.birth.to_sql(), self.address, self.social_number)
