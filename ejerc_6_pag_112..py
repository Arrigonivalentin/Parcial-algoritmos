from lista import remove, search, by_name
# Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,

# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:

# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

super_heroes = [
    {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
    },
    {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
    },
    {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
    },
    {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
    },
    {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
    },
    {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
    },
    {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
    },
    {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
    },
    {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
    },
    {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
    },
    {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
    },
    {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, es un joven héroe con un traje y habilidades arácnidas tras ser picado por una araña radiactiva."
    },
    {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
    },
    {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
    },
    {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
    },
    {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
    },
    {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
    },
    {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
    },
    {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
    },
    {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
    },
    {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
    },
    {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
    },
    {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hank Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos."
    }
]

contador_dc_comics = 0
contador_marvel_comics = 0

for heroe in super_heroes:
    print(heroe)

# a. eliminar el nodo que contiene la información de Linterna Verde
def eliminar_linterna_verde(super_heroes):
    for index, element in enumerate(super_heroes):
        if super_heroes[index]['nombre'] == "Linterna Verde":
            print()
            print("El nodo de linterna verde se eliminó correctamente")
            super_heroes.pop(index)
    return()



# b. mostrar el año de aparición de Wolverine;
def mostrar_año_aparicion_wolverine(super_heroes):
    for i in range(len(super_heroes)):
        if super_heroes[i]['nombre']=="Wolverine":
            return(super_heroes[i]['año_aparicion'])


# c. cambiar la casa de Dr. Strange a Marvel;

def cambiar_casa_doctor_strange(super_heroes):
    for index, heroes in enumerate(super_heroes):
        if super_heroes[index]['nombre']=="Doctor Strange":
            super_heroes[index]['casa_comic']="Marvel"
            return(super_heroes[index]['casa_comic'])
    return()


# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”
def biografia_armadura_traje(super_heroes):
    for i in range(len(super_heroes)):
        if 'traje' in super_heroes[i]['biografia'] or 'armadura' in super_heroes[i]['biografia']:
            print(super_heroes[i]['nombre'], "posee traje o armadura")
    return()


# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
def anterior_1963(super_heroes):
    print("estos son los super heroes que aparecieron antes de 1963: ")
    for index, element in enumerate(super_heroes):
        if super_heroes[index]['año_aparicion']<1963:
            print(super_heroes[index]['nombre'],"de", super_heroes[index]['casa_comic'])
    return()


# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
def capitana_marvel_mujer_maravilla(super_heroes):
    for index, element in enumerate(super_heroes):
        if super_heroes[index]['nombre'] == "Capitana Marvel":
            print("Capitana Marvel pertenece a: ", super_heroes[index]['casa_comic'])
        elif super_heroes[index]['nombre'] == "Mujer Maravilla":
            print("Mujer Maravilla pertenece a: ", super_heroes[index]['casa_comic'])
    return()


# g. mostrar toda la información de Flash y Star-Lord;
def mostrar_informacion(super_heroes):
    for index, element in enumerate(super_heroes):
        if element['nombre'] == "Flash":
            print("esta es toda la informacion de flash: ", super_heroes[index])
        elif element['nombre'] == "Star-Lord":
            print("esta es toda la informacion de Star-Lord: ", super_heroes[index])


# h. listar los superhéroes que comienzan con la letra B, M y S;
def letra_inicial(super_heroes):
    super_heroes.sort(key=by_name)
    print("Estos son los super heroes que comienzan con B, M, S: ")
    for element in super_heroes:
        if element['nombre'].startswith(('B', 'M', 'S')):
            print(element['nombre'])
    return()


# i. determinar cuántos superhéroes hay de cada casa de comic.
def cantidad_casa_comics(super_heroes, contador_dc_comics, contador_marvel_comics):
    for element in super_heroes:
        if element['casa_comic'] == "Marvel Comics":
            contador_marvel_comics +=1
        else:
            contador_dc_comics +=1
    print("Hay", contador_marvel_comics, "super heroes que pertenecen a Marvel Comics y", contador_dc_comics, "que pertenecen a DC Comics")
    return()




eliminar_linterna_verde(super_heroes)
print()


print("el año de aparición de wolverine es: ", mostrar_año_aparicion_wolverine(super_heroes))
print()

print("La casa de Doctor Strange ahora es: ", cambiar_casa_doctor_strange(super_heroes))
print()

biografia_armadura_traje(super_heroes)
print()

anterior_1963(super_heroes)
print()

capitana_marvel_mujer_maravilla(super_heroes)
print()

mostrar_informacion(super_heroes)
print()

letra_inicial(super_heroes)
print()

cantidad_casa_comics(super_heroes, contador_dc_comics, contador_marvel_comics)






