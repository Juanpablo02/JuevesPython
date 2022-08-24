import math

def reto1():
    contador = 0
    while contador >= 0:
        numero = int(input("Digite un numero positivo, si este es negativo cancelará el programa: "))
        contador = numero
    else: 
        print(f'Se digito un numero negativo {numero}, el programa de cerró')
    
reto1()


def reto2():
    contador = 1
    
    while contador != 0:
        print("**********************")
        print("******** Menú ********")
        print("**********************")
        print("")
        print("Digite porfavor el digito de la opcíon que desees ejecutar")
        print("0 : Salida")
        print("1 : Encuentre si el número es múltiplo de 2")
        print("2 : Encuentre la raíz cuadrada del número")
        print("3 : Sume 100 al número ingresado")
        print("4 : Eleve a la 2 el número ingresado")
        selector = int(input("Seleccionar: "))
        
        if selector == 1:
            print("**** Bienvenido aquí podras encontrar que número es múltiplo de 2 ****")
            numero = int(input("Porfavor digite un número: "))
            if numero % 2 == 0:
                print(f'El numero {numero}, si es multiplo de 2')
            else:
                print(f'El numero {numero}, no es multiplo de 2')
        elif selector == 2:
            print("**** Bienvenido aquí podras encontrar la raiz cuadrada de cualquier número ****")
            numero = int(input("Porfavor digite un número: "))
            resultado = math.sqrt(numero)
            print(f'La raiz cuadrada de {numero} es {resultado}')            
        elif selector == 3:
            print("**** Bienvenido aquí podras sumar 100 a cualquier número ****")
            numero = int(input("Porfavor digite un número: "))
            resultado = numero + 100
            print(f'El número que ingresaste es {numero} y sumandole 100 es {resultado}')
        elif selector == 4:
            print("**** Bienvenido aquí podras elevar a la 2 cualquier número ****")
            numero = int(input("Porfavor digite un número: "))
            resultado = numero ** 2
            print(f'El resultado del número {numero} elevando a la dos es {resultado}')
        elif selector == 0:
            print("**** Escogiste salir del programa, muchas gracias por visitarnos ****")
            contador = 0
        else:
            print("Porfavor digita un número valido")

reto2()

