opcion = 100
i = 0
print("*** Empanadas inteligentes ***")
print("1. Agregar Clientes")
print("2. Mostrar Cliente")
print("3. Mostrar Cedula")
print("4. Mostrar jugador por cedula")
print("0. Salir")

clientes = {}
listaclientes = []

while opcion != 0:
    opcion = int(input("Digite un opcion: "))

    if opcion == 1:
        clientes['cedula'] = input("Digite su cedula: ")
        clientes['nombre'] = input("Digite su nombre: ")

        listaclientes.insert(i,clientes)
        i = i + 1
    elif opcion == 2:
        print(clientes)
    elif opcion == 3:
        print(f'su cedula: {clientes["cedula"]}')
    elif opcion == 4:
        cedula = input("Digite la cedula del jugador: ")
        for cliente in listaclientes:
            if cliente["cedula"] == cedula:
                print(f"La cedula del jugador es: {cliente['nombre']}")  
        else:
            print("Esta cedula no esta en la base de datos")
    elif(opcion == 0):
        break
    else:
        print("Digite un opcion valida")
else:
    print("Adios")
print(clientes)
print(listaclientes)