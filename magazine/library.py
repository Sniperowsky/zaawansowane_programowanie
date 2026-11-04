class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Księgarnia w mieście {self.city} na ulicy {self.street}. Kod pocztowy {self.zip_code}. Otwarta w godzinach {self.open_hours}. Numer kontaktowy {self.phone}.'
