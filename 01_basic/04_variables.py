##
#04- Variables
#Variables para controlar datos en memoria
##

#Asignar una variable
my_name = "John"
print(my_name)

age = 25
print(age)

# Tipado dinamicos: el tipo de dato se determina en tiempo de ejecución
# que no tienes que declararlo explicitamente
name = "John"
print(type(name))

name = 25
print(type(name))

#Tipado fuerte: Python no realiza conversiones de tipo automaticas
print("Hello {my_name}, tengo {age} años")

MI_CONSTANTE = 3.1416 #UPPERCASE -> Constante
print(MI_CONSTANTE)