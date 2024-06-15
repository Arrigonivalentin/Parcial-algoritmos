# Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
# una que contenga los números pares y otra para los números impares.

lista_enteros = [3, 4, 8, 1, 9]

lista_pares= []
lista_impares= []

for n in lista_enteros:
    if n % 2==0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)
    
print(lista_pares)
print(lista_impares)
