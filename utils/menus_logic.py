# logica de los menus del programa
# Recepcion de inputs y logica de cada menu

import json
import time
from models.stateMachine import State
from models.sighting import Sighting

# Limpiar Menu
def Cleantml() :

    for i in range(30) :
        print("")

# Menu principal
def MainMenu(StateMachine: State):
    options = ["Registrar Avistamiento", "Mostrar Avistamientos", "Buscar por especie", "Buscar por fecha", "Salir"]

    # Limpiar
    Cleantml()

    #Prompt
    print("== Seleccione una opcion del menu ==")

    # Opciones
    for i, option in enumerate(options):
        print(str(i) + ".- " + option)

    print("====================================")

    # Manejar entrada del usuario
    UserOption = int(input("Opcion >> "))

    if UserOption < 0 and UserOption > 4 :
        print("Opcion Invalida\n(Opciones 1-4)")
        time.sleep(2)
        # Volver al menu principal
        StateMachine = State.MAIN_MENU
    
    else :
        # Cambiar el estado de la maquina segun la opcion seleccionada
        match UserOption:
            case 0:
                StateMachine = State.REGISTER_SIGHTING
            case 1:
                StateMachine = State.SHOW_SIGHTINGS
            case 2:
                StateMachine = State.SEARCH_BY_SPECIES
            case 3:
                StateMachine = State.SEARCH_BY_DATE
            case 4:
                StateMachine = State.EXIT

    return StateMachine

# Resgistrar Avistamiento
def RegisterSighting(SightingList, StateMachine: State):

    # Limpiar 
    Cleantml()

    # Prompt para ingresar los datos del avistamiento
    print("Ingrese los datos del avistamiento:")

    # Solicitar los datos del avistamiento
    species = input("Especie >> ")

    date = input("Fecha >> ")

    print("Ubicación: ")
    latitud = float(input("Latitud >> "))
    longitud = float(input("Longitud >> "))
    location = (latitud, longitud)

    species_number = int(input("Número de especies >> "))

    # Nueva instancia de avistamiento
    new_sighting = Sighting(species, date, location, species_number)
    SightingList.append(new_sighting)

    # Guardar la lista de avistamientos en un archivo JSON
    with open("sightings.json", "w") as file:
        json.dump([s.__dict__ for s in SightingList], file, indent=4, ensure_ascii=False)
    
    # Mensaje de confirmacion  
    print("Avistamiento registrado exitosamente.")  
    time.sleep(2)  # Pausa de 2 segundos

    # Volver al menu principal
    StateMachine = State.MAIN_MENU
    return StateMachine

# Mostrar Avistamientos
def ShowSightings(SightingList, StateMachine: State): 

    # Limpiar
    Cleantml()

    #* Mostrar Informacion en formato Tabla *
    # Cabezera
    print(f"{'-Especie-':<20}{'-Cantidad-':<12}{'-Fecha-':<12}{'-Ubicacion-':<15}")
    
    # Caracteristicas
    for i, av in enumerate(SightingList, start=1):
        linea = (
            f"{av.species:<20}"
            f"    {av.species_number:<8}"
            f"{av.date:<12}"
            f"{str(av.location):<25}"
        )

        print(linea)

    # Espera
    input("\n(Presione ENTER para continuar...)")

    # Volver al menu principal
    StateMachine = State.MAIN_MENU
    return StateMachine

# Buscar Avistamientos por especie
def SearchSpeciesSightings(SightingList, StateMachine: State):

    # Limpiar
    Cleantml()

    # Prompt
    print("======================")
    print(" Busqueda por Especie")
    print("======================")
    print("\nIngrese el nombre de la especie que esta buscando")
    Species = input("Especie >> ")

    matches = []

    # Busqueda
    for avistamiento in SightingList :
        if Species.lower() in avistamiento.species.lower() :
            matches.append(avistamiento)

    if not matches :
        print("No se encontraron coincidencias")
        time.sleep(2)
        return State.MAIN_MENU

    return ShowSightings(matches, StateMachine)


#Buscar Avistameintos por fecha

def SearchDateSightings(SightingList, StateMachine: State): 

    # Limpiar
    Cleantml()

    # Prompt
    print("====================")
    print(" Busqueda por Fecha")
    print("====================")
    print("\nIngrese La fecha en formato AAAA-MM-DD")
    date = input("Fecha >> ")

    matches = []

    # Busqueda
    for avistamiento in SightingList :
        if date in avistamiento.date :
            matches.append(avistamiento)

    if not matches :
        print("No se encontraron coincidencias")
        time.sleep(2)
        return State.MAIN_MENU

    return ShowSightings(matches, StateMachine)

