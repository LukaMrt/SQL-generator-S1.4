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

    student_id = 1
    company_id = 1
    study_id = 1
    cost_id = 1
    cost_payment_id = 1
    advance_id = 1
    indemnity_id = 1
    bill_id = 1

    # Create students
    for _ in range(randint(20, 40)):
        students.append(Student(student_id, fake.last_name(), fake.date(pattern="%d/%m"), fake.street_address(),
                                randint(1, 2) * 1000000000000 + randint(10, 90) * 10000000000 +
                                randint(1000000000, 9999999999)))
        student_id += 1

    # Create companies
    for _ in range(randint(5, 10)):
        companies.append(Company(company_id, fake.word(), fake.street_address(), randint(600000000, 799999999)))
        company_id += 1

    # Create studies
    for _ in range(randint(5, 15)):
        studies.append(
            Study(study_id, fake.word(), fake.date(pattern="%d/%m"), randint(1, 6), randint(350, 1_000), randint(10, 50),
                  float(randint(10, 30)) / 100.0))
        study_id += 1

        companies_copy = companies.copy()
        shuffle(companies_copy)
        pop_company = companies_copy.pop()
        studies[-1].company = pop_company.id

        students_copy = students.copy()
        shuffle(students_copy)
        # Create participations
        for _ in range(randint(2, studies[-1].company_price // studies[-1].student_price) // 3):

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
            for _ in range(randint(1, 5)):
                start_time += randint(86400, 86400 * 15 * studies[-1].duration)
                if start_time > end_time:
                    break

                if last_month != datetime.fromtimestamp(start_time).month and len(temp_costs) > 0:
                    costs_payments.append(Payment(cost_payment_id, datetime.fromtimestamp(start_time)))
                    cost_payment_id += 1
                    for cost in temp_costs:
                        cost.payment = costs_payments[-1].id
                    temp_costs = []
                    last_month = datetime.fromtimestamp(start_time).month

                cost = Cost(cost_id, studies[-1].id, pop.id, datetime.fromtimestamp(start_time),
                            cost_types[randint(0, len(cost_types) - 1)], randint(300, 10000) / 100.0)
                cost_id += 1
                costs.append(cost)
                temp_costs.append(cost)

            end.__add__(timedelta(days=randint(1, 10)))
            costs_payments.append(Payment(cost_payment_id, end))
            cost_payment_id += 1
            for cost in temp_costs:
                cost.payment = costs_payments[-1].id

            if end < datetime.now() and randint(0, 10) > 2:
                indemnities.append(Indemnity(indemnity_id, studies[-1].id, pop.id, end))
                indemnity_id += 1
                bills.append(Bill(bill_id, pop_company.id, studies[-1].id, end))
                bill_id += 1

            # Create advances
            advances_count = randint(0, 3)
            for _ in range(advances_count):
                max_advance = (studies[-1].student_price * participations[-1].duration) // advances_count
                advances.append(Advance(advance_id, pop.id, studies[-1].id, randint(1, max_advance)))
                advance_id += 1

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

