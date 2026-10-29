#Clase Avistamiento
class Sighting:
    def __init__(self, species, date, location, species_number):
        self.species = species
        self.date = date
        self.location = location
        self.species_number = species_number

    def __str__(self):
        return f"Especie: {self.species}, Fecha: {self.date}, Ubicación: {self.location}, Número de especies: {self.species_number}"