
class Company:
    id = 0

    def __init__(self, name, address, phone):
        self.id = Company.id
        Company.id += 1
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return "Company: " + str(self.id) + " " + self.name + " " + self.address + " " + self.phone
