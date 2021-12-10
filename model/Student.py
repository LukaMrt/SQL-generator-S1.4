from random import randint

from model.Date import Date


class Student:
    id = 0

    def __init__(self, name, birth, address, social_number):
        self.id = Student.id
        Student.id += 1
        self.name = name
        date = birth.split("/")
        self.birth = Date(int(date[0]), int(date[1]), 2003 - randint(1, 10))
        self.address = address
        self.social_number = social_number

    def __str__(self):
        return "INSERT INTO ETUDIANT VALUES ({}, '{}', {}, '{}', '{}');" \
            .format(self.id, self.name, self.birth, self.address, self.social_number)
