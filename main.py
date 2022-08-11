from ast import parse
from xml.dom.expatbuilder import parseString


print ("hola mundo, soy juan")

# Variables
#1. Datos Primitivos

nombre = "Juan Pablo "
edad = 20
estatura = 1.66
hinchaDelMejor = True
comidaFavorita = None

#2. Datos que entran por el teclado

apellido = input("Digita tu apellido porfavor: ")
peso = input("Cual es su peso?: ")

numeero1 = int(input("Digite el primer numero: "))
numeero2 = int(input("Digite el segundo numero: "))

suma = numeero1 + numeero2

print ("La suma es:",suma)
print (f'La suma es: {suma}')
print (nombre + apellido)
print (peso)



