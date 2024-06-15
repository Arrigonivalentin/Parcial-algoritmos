# Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.

lista = [1, 2, 3, 4]

respuesta = input("¿quieres ingresar un numero a la lista? (s/n): ")

while respuesta == "s":
    posicion= int(input("¿en que posicion quiere ingresar el número?: "))
    if posicion>len(lista):
        print ("la posicion debe ser de 0 y", len(lista))
    else:
        numero_agregar= int(input("ingrese el número: "))
        lista.insert(posicion, numero_agregar)
    respuesta= input("¿desea ingresar otro número? (s/n): ")

print("la lista es: ", lista)