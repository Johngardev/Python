###
# 01 - Sentencias de condicionales (if, elif, else)
# Permiten ejecutar bloques de codigo si se cumplen ciertas condiciones
###

import os
os.system('clear')

print("\n Sentencias simples de condicional")

edad = 25

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes votar")

print("\n Sentencias de condicional con else")

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Sentencias de condicional con elif")

nota = 7

if nota >= 9:
    print("Sobresaliente!")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspendido")

print("\n Condiciones multiples")

edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir!!")

# Un pueblo de Colombia (OR)

if edad >= 18 or tiene_carnet:
    print("Puedes conducir")
else:
    print("Paga la multa!!")

print("\n Condiciones anidadas")

edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes comprar cerveza")
    else:
        print("No tienes dinero") 
else:
    print("Eres menor de edad")

#Mas facil
if edad < 18:
    print("Eres menor de edad")
elif not tiene_dinero:
    print("No tienes dinero")
else:
    print("Puedes comprar cerveza")