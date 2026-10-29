# Maquina de estados para el flujo del programa

import enum

class State(enum.Enum):
    MAIN_MENU = 1
    REGISTER_SIGHTING = 2
    SHOW_SIGHTINGS = 3
    SEARCH_BY_SPECIES = 4
    SEARCH_BY_DATE = 5
    EXIT = 6