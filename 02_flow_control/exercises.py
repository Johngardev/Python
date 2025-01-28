###
# EJERCICOS IF
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

### SOLUCION 1 ###

#numberOne = input("Ingrese el primer numero: ")
#numberTwo = input("Ingrese el segundo numero: ")

#if numberOne > numberTwo:
#    print("El primero numero es mayor")
#elif numberTwo > numberOne:
#    print("El segundo numero es mayor")
#else:
#    print("Son numeros iguales")

#-----------------------------------------------------------------------------------------#

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

### SOLUCION 2 ###

#a = input("Ingrese el primer numero a operar: ")
#b = input("Ingrese el segundo numero a operar: ")
#op = input("Ingrese que operacion desea realizar (+), (-), (*) o (/): ")

#if op == "+":
#    print("Sumar: ", int(a) + int(b))
#elif op == "-":
#    print("Restar: ", int(a) - int(b))
#elif op == "*":
#    print("Multiplicar: ", int(a) * int(b))
#elif op == "/":
#    if b == 0:
#        print("Indefinido: division por cero.")
#    else:
#        print("Division: ", int(a) / int(b))
#else:
#    print("Syntax error")

#-----------------------------------------------------------------------------------------#

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

### SOLUCION 3 ###

#annio = input("Ingrese año: ")

#if int(annio) % 4 == 0:
#    if int(annio) % 100 == 0:
#        int(annio) % 400 == 0
#    else:
#        print("Es bisiesto")
#else:
#    print("No es bisiesto")
    


#-----------------------------------------------------------------------------------------#

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

### SOLUCION 3 ###

#edad = input("Ingrese edad :")

#if int(edad) >= 0 and int(edad) <= 2:
#    print("Eres bebe")
#elif int(edad) >= 3 and int(edad) <= 12:
#    print("Eres un Niño")
#elif int(edad) >= 13 and int(edad) <= 17:
#    print("Eres adolescente")
#elif int(edad) >= 18 and int(edad) <= 64:
#    print("Eres Adulto")
#elif int(edad) >= 65:
#    print("Eres Adulto mayor")
#else:
#    print("error")
#-----------------------------------------------------------------------------------------#

###
# EJERCICOS LIST
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

#-----------------------------------------------------------------------------------------#

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

#-----------------------------------------------------------------------------------------#

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

#-----------------------------------------------------------------------------------------#

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

###
# EJERCICOS LIST METHODS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.