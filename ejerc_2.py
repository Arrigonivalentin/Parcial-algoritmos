# Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.


caracteres = ["g", "a", "l", "m", "e"]
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
lista_sin_vocales = []

for n in caracteres:
    if n not in vocales:
        lista_sin_vocales.append(n)

print(lista_sin_vocales)