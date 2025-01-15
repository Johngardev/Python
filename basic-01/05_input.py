##
#05 - Entrada de usuario(input()) - version simplificada
#La funcion input() permite al usuario ingresar datos a traves de la consola
##

nombre = input("Ingresa tu nombre: ")
print("Hola {nombre}, un gusto")

age = input("Ingresa tu edad: ")
age = int(age)
print("Tienes {age} años")

country, city = input("Ingresa tu pais y ciudad: ").split()
print("Vives en {city}, {country}")