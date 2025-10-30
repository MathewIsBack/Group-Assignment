class Customer:

    def __init__(self, name, id_number):
        self.name = name 
        self.id_number = id_number

    def __str__(self):
        return f"{self.name} (ID: {self.id_number})"