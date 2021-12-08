from random import randint

from model.Date import Date


class Study:
    id = 0

    def __init__(self, name, date, duration, company_price, student_price, detention):
        self.id = Study.id
        Study.id += 1
        self.name = name
        date = date.split("/")
        self.birth = Date(int(date[0]), int(date[1]), 2021 - randint(1, 5))
        self.duration = duration
        self.company_price = company_price
        self.student_price = student_price
        self.detention = detention
