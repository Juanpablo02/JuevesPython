def reto1():
    numero = int(input("Porfavor digite un numero para saber si es multiplo de 5: "))
    if numero % 5 == 0:
        print(f'El número {numero}, si es multiplo de 5')
    else:
        print(f'El número {numero}, no es multiplo de 5')
        
reto1()


def reto2():
    numero = int(input("Porfavor digite un numero para saber si es multiplo de 3: "))
    if numero % 3 == 0:
        print(f'El número {numero}, si es multiplo de 3')
    else:
        print(f'El número {numero}, no es multiplo de 3')
        
reto2()
    
    
def reto3():
    numero1 = int(input("Porfavor digite un numero: "))
    numero2 = int(input("Porfavor digite un numero: "))
    if numero1 > numero2:
        print(f'El numero {numero1} es mayor que el numero {numero2}')
    else:
        print(f'El numero {numero2} es mayor que el numero {numero1}')
        
reto3()


def reto4():
    dineroJuan = int(input("Ingrese la cantidad de dinero que tiene Juan: "))
    dineroCamila = dineroJuan / 2
    dineroRicardo = (dineroJuan + dineroCamila) / 2;
    dineroConjunto = dineroJuan + dineroCamila + dineroRicardo
    print(f'Dinero de Juan: {dineroJuan}')
    print(f'Dinero de Camila: {dineroCamila}')
    print(f'Dinero de Ricardo: {dineroRicardo}')
    print(f'Dinero de los 3: {dineroConjunto}')
    
reto4()


def reto5():
    ventasRealizadas = int(input("Digite el numero de ventas realizadas: "))
    pagoConVentas = 3500000 + (ventasRealizadas * 1500000)
    pagoVentas = pagoConVentas - (pagoConVentas * 0.05)
    print(f'El salario mensual es de {pagoVentas}')
    
reto5()