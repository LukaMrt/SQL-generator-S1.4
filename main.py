from random import randint, shuffle
from datetime import datetime
from datetime import timedelta
from faker import *

from model.Advance import Advance
from model.Bill import Bill
from model.Company import Company
from model.Cost import Cost
from model.Indemnity import Indemnity
from model.Participation import Participation
from model.Payment import Payment
from model.Student import Student
from model.Study import Study


def fill_database(file_name):

    file = open(file_name, "w")

    fake = Faker()

    cost_types = [
        "Materiel",
        "Repas",
        "Transport",
        "Logiciel",
        "Abonnement",
        "Divers"
    ]

    students = []
    companies = []
    studies = []
    participations = []
    costs = []
    costs_payments = []
    advances = []
    indemnities = []
    bills = []

    # Create students
    for _ in range(randint(40, 100)):
        students.append(Student(fake.last_name(), fake.date(pattern="%d/%m"), fake.street_address(),
                                randint(1, 2) * 1000000000000 + randint(10, 90) * 100000000000 +
                                randint(1000000000, 9999999999)))

    # Create companies
    for _ in range(randint(10, 30)):
        companies.append(Company(fake.word(), fake.street_address(), fake.phone_number()))

    # Create studies
    for _ in range(randint(10, 50)):
        studies.append(
            Study(fake.word(), fake.date(pattern="%d/%m"), randint(1, 6), randint(100, 400), randint(10, 50),
                  float(randint(10, 30)) / 100.0))

        companies_copy = companies.copy()
        shuffle(companies_copy)
        pop_company = companies_copy.pop()
        studies[-1].company = pop_company.id

        # Create participations
        for _ in range(randint(2, studies[-1].company_price // studies[-1].student_price) - 1):

            students_copy = students.copy()
            shuffle(students_copy)
            pop = students_copy.pop()

            if studies[-1].in_charge == -1:
                studies[-1].in_charge = pop.id

            participations.append(Participation(pop.id, studies[-1].id, randint(5, min(30, studies[-1].duration * 20))))

            date = studies[-1].date
            start = datetime(date.year, date.month, date.day)
            start_time = start.timestamp()
            end = start.__add__(timedelta(weeks=studies[-1].duration * 4))
            end_time = end.timestamp()

            # Create costs
            temp_costs = []
            last_month = start.month
            for _ in range(randint(1, 10)):
                start_time += randint(86400, 86400 * 15 * studies[-1].duration)
                if start_time > end_time:
                    break

                if last_month != datetime.fromtimestamp(start_time).month and len(temp_costs) > 0:
                    costs_payments.append(Payment(datetime.fromtimestamp(start_time)))
                    for cost in temp_costs:
                        cost.payment = costs_payments[-1].id
                    temp_costs = []
                    last_month = datetime.fromtimestamp(start_time).month

                cost = Cost(studies[-1].id, pop.id, datetime.fromtimestamp(start_time),
                            cost_types[randint(0, len(cost_types) - 1)], randint(300, 10000) / 100.0)
                costs.append(cost)
                temp_costs.append(cost)

            end.__add__(timedelta(days=randint(1, 10)))
            costs_payments.append(Payment(end))
            for cost in temp_costs:
                cost.payment = costs_payments[-1].id

            if end < datetime.now() and randint(0, 10) > 2:
                indemnities.append(Indemnity(studies[-1].id, pop.id, end))
                bills.append(Bill(pop_company.id, studies[-1].id, end))

            # Create advances
            advances_count = randint(0, 3)
            for _ in range(advances_count):
                max_advance = (studies[-1].student_price * participations[-1].duration) // advances_count
                advances.append(Advance(pop.id, studies[-1].id, randint(1, max_advance)))

    for student in students:
        file.write(student.to_sql() + "\n")
    file.write("\n")

    for company in companies:
        file.write(company.to_sql() + "\n")
    file.write("\n")

    for study in studies:
        file.write(study.to_sql() + "\n")
    file.write("\n")

    for advance in advances:
        file.write(advance.to_sql() + "\n")
    file.write("\n")

    for bill in bills:
        file.write(bill.to_sql() + "\n")
    file.write("\n")

    for payment in costs_payments:
        file.write(payment.to_sql() + "\n")
    file.write("\n")

    for cost in costs:
        file.write(cost.to_sql() + "\n")
    file.write("\n")

    for indemnity in indemnities:
        file.write(indemnity.to_sql() + "\n")
    file.write("\n")

    for participation in participations:
        file.write(participation.to_sql() + "\n")
    file.write("\n")

    file.write("COMMIT;\n")
    file.close()


if __name__ == '__main__':

    for i in range(1, 11):
        fill_database("data/data_" + str(i) + ".sql")

