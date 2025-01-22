###
# 04 - Listas Metodos
# Los metodos mas importantes para trabajar con listas
###

# Creacion de listas
print("\n Creacion de listas")
lista1 = ['a', 'b', 'c', 'd'] 

# Añadir elementos a la lista
print("\n Añadir elementos a la lista")
lista1.append('e')
print(lista1) # ['a', 'b', 'c', 'd', 'e']

# Insertar elementos en la lista
print("\n Insertar elementos en la lista")
lista1.insert(2, 'z')
print(lista1) # ['a', 'b', 'z', 'c', 'd', 'e']

lista1.extend(['f', 'g', 'h']) # Añade una lista al final

# Eliminar elementos de la lista
print("\n Eliminar elementos de la lista")
lista1.remove('z') # Elimina el primer elemento con el valor 'z'

lista1.pop() # Elimina el ultimo elemento de la lista

# Ordenar elementos de la lista
print("\n Ordenar elementos de la lista")
lista2 = [3, 5, 1, 4, 2]
lista2.sort() # Ordena la lista de menor a mayor
print(lista2) # [1, 2, 3, 4, 5]