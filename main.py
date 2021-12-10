from random import randint, shuffle
from time import time
from datetime import datetime
from datetime import timedelta
from faker import *

from model.Company import Company
from model.Cost import Cost
from model.Payment import Payment
from model.Student import Student
from model.Study import Study


def social_number():
    return randint(1, 2) * 1000000000000 + randint(10, 90) * 100000000000 + randint(
        1000000000, 9999999999)


if __name__ == '__main__':

    file = open("sql_script.sql", "w")

    fake = Faker()

    students = []
    companies = []
    studies = []
    members = []
    costs = []
    costs_payments = []

    advances = []
    indemnities = []

    for _ in range(randint(40, 100)):
        students.append(Student(fake.last_name(), fake.date(pattern="%d/%m"), fake.street_address(), social_number()))
        file.write(str(students[-1]) + "\n")
    file.write("\n")

    for _ in range(randint(10, 30)):
        companies.append(Company(fake.word(), fake.street_address(), fake.phone_number()))
        file.write(str(companies[-1]) + "\n")
    file.write("\n")

    for _ in range(randint(10, 50)):
        studies.append(
            Study(fake.word(), fake.date(pattern="%d/%m"), randint(1, 6), randint(100, 400), randint(10, 40),
                  float(randint(10, 30)) / 100.0))

        companies_copy = companies.copy()
        shuffle(companies_copy)
        studies[-1].company = companies_copy.pop().id

        students_copy = students.copy()
        shuffle(students_copy)
        for _ in range(randint(2, studies[-1].company_price // studies[-1].student_price) - 1):

            pop = students_copy.pop()

            if studies[-1].in_charge == -1:
                studies[-1].in_charge = pop.id

            members.append((pop.id, studies[-1].id, randint(5, studies[-1].duration * 20)))
            date = studies[-1].date
            start = datetime(date.year, date.month, date.day)
            time = start.timestamp()

            end = start.__add__(timedelta(weeks=studies[-1].duration * 4))
            time2 = end.timestamp()
            temp_costs = []

            for _ in range(randint(1, 10)):
                time += randint(86400 * 2, 86400 * 31 * studies[-1].duration)
                if time > time2:
                    break

                cost = Cost(studies[-1].id, pop.id, datetime.fromtimestamp(time), '', randint(300, 10000) / 100.0)
                costs.append(cost)
                temp_costs.append(cost)

                if randint(0, 10 > 7):
                    time += 86400
                    costs_payments.append(Payment(datetime.fromtimestamp(time)))
                    for cost in temp_costs:
                        cost.payment = costs_payments[-1].id

        file.write(str(studies[-1]) + "\n")
    file.write("\n")

    for member in members:
        file.write("INSERT INTO PARTICIPATION VALUES ({}, {}, {});\n".format(member[0], member[1], member[2]))
    file.write("\n")

    for cost in costs:
        file.write(str(cost) + "\n")
    file.write("\n")

    for payment in costs_payments:
        file.write(str(payment) + "\n")
    file.write("\n")

    file.write("COMMIT;\n")
