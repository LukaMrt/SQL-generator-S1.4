class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def is_before(self, other):
        if self.year < other.year:
            return True

        if self.year == other.year:
            if self.month < other.month:
                return True

            if self.month == other.month:
                return self.day < other.day

        return False

    def is_after(self, other):
        return not self.is_before(other)

    def __str__(self):
        return "TO_DATE('{}/{}/{}', 'DD/MM/YYYY')" \
            .format(self.day if self.day > 9 else '0' + str(self.day),
                    self.month if self.month > 9 else '0' + str(self.month), self.year)
