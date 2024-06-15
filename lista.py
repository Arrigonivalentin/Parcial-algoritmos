def by_name(item):
    return item['nombre']

def by_temp(item):
    return item['temp']

def by_tournament(item):
    return item['torneos ganados']

def batallas_ganadas(item):
    return item['batallas ganadas']


def by_house(item):
    return item['casa_comic']+item['nombre']

def by_level(item):
    return item['nivel']


def show_list_list(title, subtitle, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index+1, elemento['nombre'])
        print(f"    {subtitle}")
        for second_index, second_element in enumerate(elemento['pokemones']):
            print('    ', second_index, second_element)
    print()


def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index

def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)