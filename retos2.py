import math

def reto1():
    contador = 0
    suma = 0
    while contador >= 0:
        numero = int(input("Digite un numero positivo, si este es negativo cancelará el programa: "))
        if numero >= 0:
            suma = numero + suma
        else:
            contador = numero
    print(f'Se digito un numero negativo la suma es {suma}, el programa de cerró')
    
#reto1()


def reto2():
    contador = 1
    
    while contador != 0:
        print("**********************")
        print("******** Menú ********")
        print("**********************")
        print("")
        print("Digite porfavor el digito de la opcíon que desees ejecutar")
        print("")
        print("0 : Salida")
        print("1 : Encuentre si el número es múltiplo de 2")
        print("2 : Encuentre la raíz cuadrada del número")
        print("3 : Sume 100 al número ingresado")
        print("4 : Eleve a la 2 el número ingresado")
        print("")
        selector = int(input("Seleccionar: "))
        
        if selector == 1:
            contador1 = 1
            while contador1 != 0:
                print("**** Bienvenido aquí podras encontrar que número es múltiplo de 2 ****")
                print("")
                numero = int(input("Porfavor digite un número: "))
                print("")
                if numero % 2 == 0:
                    print(f'-> El numero {numero}, si es multiplo de 2')
                    print("")
                else:
                    print(f'-> El numero {numero}, no es multiplo de 2')
                    print("")
                print("*** Deseas seguir digitando números o deseas salir al menú? ***")
                print("")
                print("0 : Si deseas salir al menú")
                print("1 : Si deseas seguir digitando numeros")
                print("")
                contador1 = int(input("Selecciona: "))
                if contador1 == 0:
                    contador1 = 0
                    
        elif selector == 2:
            contador1 = 1
            while contador1 != 0:
                print("**** Bienvenido aquí podras encontrar la raiz cuadrada de cualquier número ****")
                print("")
                numero = int(input("Porfavor digite un número: "))
                print("")
                resultado = math.sqrt(numero)
                print(f'-> La raiz cuadrada de {numero} es {resultado}')  
                print("")
                print("*** Deseas seguir digitando números o deseas salir al menú? ***")
                print("")
                print("0 : Si deseas salir al menú")
                print("1 : Si deseas seguir digitando numeros")
                print("")
                contador1 = int(input("Selecciona: "))
                if contador1 == 0:
                    contador1 = 0          
        elif selector == 3:
            contador1 = 1
            while contador1 != 0:
                print("**** Bienvenido aquí podras sumar 100 a cualquier número ****")
                print("")
                numero = int(input("Porfavor digite un número: "))
                print("")
                resultado = numero + 100
                print(f'-> El número que ingresaste es {numero} y sumandole 100 es {resultado}')
                print("")
                print("*** Deseas seguir digitando números o deseas salir al menú? ***")
                print("")
                print("0 : Si deseas salir al menú")
                print("1 : Si deseas seguir digitando numeros")
                print("")
                contador1 = int(input("Selecciona: "))
                if contador1 == 0:
                    contador1 = 0      
        elif selector == 4:
            contador1 = 1
            while contador1 != 0:
                print("**** Bienvenido aquí podras elevar a la 2 cualquier número ****")
                print("")
                numero = int(input("Porfavor digite un número: "))
                print("")
                resultado = numero ** 2
                print(f'-> El resultado del número {numero} elevando a la dos es {resultado}')
                print("")
                print("*** Deseas seguir digitando números o deseas salir al menú? ***")
                print("")
                print("0 : Si deseas salir al menú")
                print("1 : Si deseas seguir digitando numeros")
                print("")
                contador1 = int(input("Selecciona: "))
                if contador1 == 0:
                    contador1 = 0      
        elif selector == 0:
            print("")
            print("**** Escogiste salir del programa, muchas gracias por visitarnos ****")
            break
        else:
            print("Porfavor digita un número valido")

#reto2()

def reto3():
    contador = 1
    numero = 1
    print(numero)
    numero = numero + 11
    print(numero)
    while contador != 0:
        numero = numero + 12
        print(numero)
        if numero >= 200:
            contador = 0
            
#reto3()

def reto4():
    contador = 0
    contadorNegativo = 0
    while contador < 20:
        numero = int(input("Digite un numero ya sea negativo o positivo: "))
        if numero < 0:
            contadorNegativo += 1
        contador += 1
    
    print(f'Fueron ingresados {contadorNegativo} numeros negativos')

#reto4()
