from random import randint, shuffle

from faker import *

from model.Company import Company
from model.Student import Student
from model.Study import Study

if __name__ == '__main__':

    file = open("sql_script.sql", "w")

    fake = Faker()

    students = []
    companies = []
    studies = []
    members = []

    advances = []
    costs = []
    costs_payments = []
    indemnities = []

    for _ in range(randint(20, 100)):
        students.append(Student(fake.last_name(), fake.date(pattern="%d/%m"), fake.street_address(),
                                randint(1, 2) * 1000000000000 + randint(10, 90) * 100000000000 + randint(
                                    1000000000, 9999999999)))
        file.write(str(students[-1]))

    for _ in range(randint(10, 30)):
        companies.append(Company(fake.word(), fake.street_address(), fake.phone_number()))

    for _ in range(randint(4, len(students) - 5)):
        studies.append(Study(fake.word(), fake.date(pattern="%d/%m"), randint(1, 6), randint(20, 200), randint(10, 40),
                             float(randint(30, 70)) / 100.0))

        students_copy = students.copy()
        shuffle(students_copy)
        in_charge = None
        for _ in range(randint(3, 15)):

            if in_charge is None:
                pop = students_copy.pop()
                in_charge = pop
                members.append((pop, studies[-1], randint(5, studies[-1].duration * 20)))
                continue

            members.append((students_copy.pop(), studies[-1], randint(5, studies[-1].duration * 20)))

    file.write("COMMIT;\n")
