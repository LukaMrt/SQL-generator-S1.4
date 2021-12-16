class Company:

    def __init__(self, id, name, address, phone):
        self.id = id
        self.name = name
        self.address = address

        self.phone = str(phone % 100)
        phone //= 100
        self.phone = str(phone % 100) + "." + self.phone
        phone //= 100
        self.phone = str(phone % 100) + "." + self.phone
        phone //= 100
        self.phone = str(phone % 100) + "." + self.phone
        phone //= 100
        self.phone = "0" + str(phone % 10) + "." + self.phone

    def to_sql(self) -> str:
        return "INSERT INTO ENTREPRISE (NOM_ENTREPRISE, ADRESSE_ENTREPRISE, TELEPHONE_ENTREPRISE) " \
               " VALUES ('{}', '{}', '{}');" \
            .format(self.name, self.address, self.phone)
