###
# 03 - Listas
# Secuencia mutable de elementos
# Pueden contener elementos de diferentes tipos
###

#Creacion de listas
print("\n Creacion de listas")
lista1 = [1, 2, 3, 4, 5] # Lista de enteros
lista2 = ["manzana", "pera", "uva"] # Lista de cadenas
lista3 = [1, "manzana", 3.14, True] # Lista de diferentes tipos

lista_vacia = [] # Lista vacia
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Lista de listas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matriz)

# Acceso a elementos por indice
print("\n Acceso a elementos por indice")
print(lista1[0]) # 1
print(lista2[1]) # pera
print(lista2[-1]) # uva

print(lista_de_listas[1][1]) # 5

# Modificacion de elementos
print("\n Modificacion de elementos")
lista1[0] = 100
print(lista1) # [100, 2, 3, 4, 5]

# Slicing (Rebanado) de listas
print("\n Slicing de listas")
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista1[0:3]) # [1, 2, 3]

# MORE MAGIC
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista1[::2]) # devuelve indices pares
print(lista1[::-1]) # devuelve indices inversos

# Añadir elementos a la lista
print("\n Añadir elementos a la lista")
lista1 = lista1 + [11, 12, 13] #forma larga y menos eficiente
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

lista1 += [14, 15, 16] #forma corta y mas eficiente
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Obtener longitud de la lista
print("\n Longitud de la lista")
print(len(lista1)) # 16