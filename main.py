# Registro de avistamientos de fauna

#* Modulos
from re import match
import json
import time
from pathlib import Path
from models.sighting import Sighting
from models.stateMachine import State
from utils import menus_logic

#* Global Variables
SightingList = []  # Lista para almacenar los avistamientos registrados
SightingsFilePath = Path("sightings.json") 

#* Funciones

# Mensaje de bienvenida
def WelcomeMessage():
    print("Bienvenido a esta demo de registro de avistamientos de fauna")
    print("Sera capaz de registrar y buscar avistamientos")
    time.sleep(3)

# Lectura del archivo JSON de avistamientos
def LoadSightingsFromJSON():
    global SightingList
    if SightingsFilePath.exists():
        with open(SightingsFilePath, "r") as file:
            sightings_data = json.load(file)
            SightingList = [Sighting(**s) for s in sightings_data]
    else:
        SightingList = []  # Inicializar como lista vacía si no existe el archivo

#* Main Function
def main() :

    global SightingList

    # Init State Machine
    StateMachine = State.MAIN_MENU

    # Leer sightings.json
    LoadSightingsFromJSON()

    # Mensaje de bienvenida
    WelcomeMessage()

    #* Bucle Principal
    while True:

        # State machine logic
        match StateMachine:
            case State.MAIN_MENU:
                # Logica para el menu principal
                StateMachine = menus_logic.MainMenu(StateMachine)
            case State.REGISTER_SIGHTING:
                # Lógica para registrar avistamiento
                StateMachine = menus_logic.RegisterSighting(SightingList, StateMachine)
            case State.SHOW_SIGHTINGS:
                # Lógica para mostrar avistamientos
                StateMachine =  menus_logic.ShowSightings(SightingList, StateMachine)
            case State.SEARCH_BY_SPECIES:
                # Lógica para buscar por especie
                StateMachine = menus_logic.SearchSpeciesSightings(SightingList, StateMachine)
            case State.SEARCH_BY_DATE:
                # Lógica para buscar por fecha
                StateMachine = menus_logic.SearchDateSightings(SightingList, StateMachine)
            case State.EXIT:
                break  # Salir del bucle principal y terminar el programa


    # Salir del programa
    print("Saliendo del programa...")
    time.sleep(2)  # Pausa de 2 segundos

if __name__ == "__main__":
    main()