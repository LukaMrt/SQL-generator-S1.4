class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def to_sql(self) -> str:
        return "TO_DATE('{}/{}/{}', 'DD/MM/YYYY')" \
            .format(self.day if self.day > 9 else '0' + str(self.day),
                    self.month if self.month > 9 else '0' + str(self.month), self.year)
