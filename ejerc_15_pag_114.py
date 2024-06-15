# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
# tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver

# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

# a. obtener la cantidad de Pokémons de un determinado entrenador;

# b. listar los entrenadores que hayan ganado más de tres torneos;

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;

# d. mostrar todos los datos de un entrenador y sus Pokémos;

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);

# g. el promedio de nivel de los Pokémons de un determinado entrenador;

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;

# i. mostrar los entrenadores que tienen Pokémons repetidos;

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

from lista import by_name, search, show_list_list, by_tournament, batallas_ganadas, by_level
from random import choice

entrenadores = [
    {
        "nombre": "clair",
        "torneos ganados": 8,
        "batallas perdidas": 10,
        "batallas ganadas": 34,
    },
    {
        "nombre": "brandon",
        "torneos ganados": 5,
        "batallas perdidas": 8,
        "batallas ganadas": 51,
    },
    {
        "nombre": "whitney",
        "torneos ganados": 5,
        "batallas perdidas": 4,
        "batallas ganadas": 41,
    },
    {
        "nombre": "diantha",
        "torneos ganados": 2,
        "batallas perdidas": 25,
        "batallas ganadas": 13
    }
]


pokemons = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None,
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": 'planta'
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno",
    },
    {
        "nombre": "Tyrantrum",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico",
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "agua",
        "subtipo": None,
    },
    {
        "nombre": "Terrakion",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "volador",
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra",
    },
    {
        "nombre": "Wingull",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra",
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": 'planta',
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": 'volador',
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None,
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Blastoise",
        "nivel": 29,
        "tipo": "siniestro",
        "subtipo": 'tierra',
    }]


lista_entrenadores = []

contador_pokemones = 0

nombres_pokemones = ["Pikachu", "Charizard", "Bulbasaur", "Tyrantrum", "Psyduck", "Terrakion", "Onix", "Wingull", "Vulpix", "Blastoise", "Umbreon", "Nidoking"]


nombres = ["clair", "brandon", "whitney", "diantha"]

for entrenador in entrenadores:
    entrenador.update({'pokemones':[]})
    lista_entrenadores.append(entrenador)



for pokemon in pokemons:
    pos = search(lista_entrenadores, 'nombre', choice(nombres))
    if pos is not None:
        lista_entrenadores[pos]['pokemones'].append(pokemon)
    else:
        print("no existe el entrenador")


lista_entrenadores.sort(key=by_name)


show_list_list('Entrenadores:', ' Pokemones:', lista_entrenadores)


# a. obtener la cantidad de Pokémons de un determinado entrenador

def cantidad_pokemones(lista_entrenadores):
    pos = search(lista_entrenadores, 'nombre', 'clair')
    nombre = lista_entrenadores[pos]['nombre']
    if pos is not None:
        return(print("la cantidad de pokemones de", nombre, "es:", len(lista_entrenadores[pos]['pokemones'])))
    else:
        print("el entrenador no existe")
    return()




# b. listar los entrenadores que hayan ganado más de tres torneos;
lista_entrenadores.sort(key=by_tournament)

def mas_tres_torneos(lista_entrenadores):
    print("estos son los entrenadores que ganaron más de tres torneos ordenados de menor a mayor: ")
    for index, element in enumerate(lista_entrenadores):
        if element['torneos ganados']>3:
            print(index, element['nombre'])
    return()


# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados

def pokemon_mayor_nivel(lista_entrenadores):
    lista_entrenadores.sort(key=by_tournament,reverse=True)
    pos = 0
    nombre_mayor_torneo = lista_entrenadores[pos]['nombre']
    if pos is not None:
        lista_entrenadores[pos]['pokemones'].sort(key=by_level, reverse=True)
        pokemon_nivel =  lista_entrenadores[pos]['pokemones'][0]
    print("El entrenador con más torneos ganados es", nombre_mayor_torneo, "y su pokemon de mayor nivel es: ", pokemon_nivel)




# d. mostrar todos los datos de un entrenador y sus Pokémos;
def mostrar_datos(lista_entrenadores):
    pos_2 = search(lista_entrenadores, 'nombre', 'whitney')
    print("Estos son todos los datos de: ", lista_entrenadores[pos_2]['nombre'])
    print (lista_entrenadores[pos_2])
    return()


# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %
def mayor_79(lista_entrenadores):
    print("Estos son los entrenadores que superan el 79 porciento de batallas ganadas: ")
    for i in range(len(lista_entrenadores)):
        batallas_totales = lista_entrenadores[i]['batallas ganadas'] + lista_entrenadores[i]['batallas perdidas']
        porcentaje = (lista_entrenadores[i]['batallas ganadas'] * 100) / batallas_totales
        if porcentaje > 79:
            print(lista_entrenadores[i]['nombre'])
    return()


# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);

def pokemones_fuego_planta(lista_entrenadores):
    print("Estos son los entrenadores que tienen pokemones de tipo Fuego y subtipo planta:")
    for index, element in enumerate(lista_entrenadores):
        pos_3 = search(lista_entrenadores, 'nombre', nombres[index])
        if pos_3 is not None:
            pos_fuego = search(lista_entrenadores[pos_3]['pokemones'], 'tipo', 'Fuego')
            if pos_fuego is not None:
                pos_planta = search(lista_entrenadores[pos_3]['pokemones'], 'subtipo', 'planta')
                if pos_planta is not None:
                    print(lista_entrenadores[pos_3]['nombre'])
    return()


def pokemones_agua_volador(lista_entrenadores):
    print("Estos son los entrenadores que tienen pokemones de tipo agua y subtipo volador:")
    for index, element in enumerate(lista_entrenadores):
        pos_4 = search(lista_entrenadores, 'nombre', nombres[index])
        if pos_4 is not None:
            pos_agua = search(lista_entrenadores[pos_4]['pokemones'], 'tipo', 'Agua')
            if pos_agua is not None: 
                pos_volador = search(lista_entrenadores[pos_4]['pokemones'], 'subtipo', 'volador')
                if pos_volador is not None:
                    print(lista_entrenadores[pos_4]['nombre'])
    return()

# g. el promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel(lista_entrenadores):
    total_nivel = 0
    cant_pokemons = 0
    pos = search(lista_entrenadores, 'nombre', 'clair')
    if pos is not None:
        nombre = lista_entrenadores[pos]['nombre']
        for pokemon in lista_entrenadores[pos]['pokemones']:
            total_nivel = total_nivel + pokemon['nivel']
            cant_pokemons += 1
    promedio = total_nivel/cant_pokemons
    print("El promedio de nivel de los pokemones de", nombre, " es: ", promedio)
    return()


# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
def cantidad_entrenadores(lista_entrenadores):
    total_entrenadores = 0
    for index, element in enumerate(lista_entrenadores):
        pos = search(lista_entrenadores, 'nombre', nombres[index])
        if pos is not None:
            pos_pokemon = search(lista_entrenadores[pos]['pokemones'], 'nombre', "Blastoise")
            if pos_pokemon is not None:
                total_entrenadores+=1
    print("la cantidad de entrenadores de Blastoise es: ", total_entrenadores)
    return()

# i. mostrar los entrenadores que tienen Pokémons repetidos

def pokemon_repetidos(lista_entrenadores):
    for index, entrenador in enumerate(lista_entrenadores):
        repetidos=[]
        for index_2, pokemon in enumerate (entrenador['pokemones']):
            for nextPokemon in range (index_2+1,len(entrenador['pokemones'])):
                if pokemon['nombre'] == entrenador['pokemones'][nextPokemon]['nombre']:
                    if pokemon['nombre'] not in repetidos:
                        repetidos.append(pokemon['nombre'])
        if len(repetidos)>0:
            print("Los pokemones repetidos son ",repetidos, "y pertenecen a ", lista_entrenadores[index]['nombre'])
    return()



# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;

def buscar_Tyrantrum(lista_entrenadores):
    for index, element in enumerate(lista_entrenadores):
        nombre = element['nombre']
        pos_6 = search(lista_entrenadores, 'nombre', nombre)
        if pos_6 is not None:
            pos_tyrantrum = search(lista_entrenadores[pos_6]['pokemones'], 'nombre', 'Tyrantrum')
            if pos_tyrantrum is not None:
                print(element['nombre'], "posee a Tyrantrum")
    return()

def buscar_Terrakion(lista_entrenadores):
    for index, element in enumerate(lista_entrenadores):
        nombre = element['nombre']
        pos_7 = search(lista_entrenadores, 'nombre', nombre)
        if pos_7 is not None:
            pos_terrakion = search(lista_entrenadores[pos_7]['pokemones'], 'nombre', 'Terrakion')
            if pos_terrakion is not None:
                print(element['nombre'], "posee a Terrakion")
    return()

def buscar_Wingull(lista_entrenadores):
    for index, element in enumerate(lista_entrenadores):
        nombre = element['nombre']
        pos_8 = search(lista_entrenadores, 'nombre', nombre)
        if pos_8 is not None:
            pos_Wingull = search(lista_entrenadores[pos_8]['pokemones'], 'nombre', 'Wingull')
            if pos_Wingull is not None:
                print(element['nombre'], "posee a Wingull")
    return()


# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

def encontrar_pokemon(lista_entrenadores, nombres, nombres_pokemones):
    print("nombres de los entrenadores: ", nombres)

    nombre_entrenador = input("ingrese el nombre del entrenador: ")

    print("nombres de los pokemones: ", nombres_pokemones)

    nombre_pokemon = input("ingrese el nombre del pokemon: ")
    print()
    pos_entrenador = search(lista_entrenadores, 'nombre', nombre_entrenador)
    if pos_entrenador is not None:
        pos_pokemon = search(lista_entrenadores[pos_entrenador]['pokemones'], 'nombre', nombre_pokemon)
        if pos_pokemon is not None:
            print(nombre_entrenador, "posee a", nombre_pokemon, "estos son los datos del pokemon: ")
            print(lista_entrenadores[pos_entrenador]['pokemones'][pos_pokemon])
            print()
            print("Estos son los datos del entrenador: ")
            print(lista_entrenadores[pos_entrenador])
        else:
            print(nombre_entrenador, "no posee a", nombre_pokemon)
    return()


cantidad_pokemones(lista_entrenadores)
print()

mas_tres_torneos(lista_entrenadores)
print()

pokemon_mayor_nivel(lista_entrenadores)
print()

mostrar_datos(lista_entrenadores)
print()

mayor_79(lista_entrenadores)
print()

pokemones_fuego_planta(lista_entrenadores)
print()

pokemones_agua_volador(lista_entrenadores)
print()

promedio_nivel(lista_entrenadores)
print()

cantidad_entrenadores(lista_entrenadores)
print()

pokemon_repetidos(lista_entrenadores)
print()

buscar_Tyrantrum(lista_entrenadores)
print()

buscar_Terrakion(lista_entrenadores)
print()

buscar_Wingull(lista_entrenadores)
print()

encontrar_pokemon(lista_entrenadores, nombres, nombres_pokemones)