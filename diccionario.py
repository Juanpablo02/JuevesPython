diccionario = {
    'nombre':'Juan Pablo',
    'apellido':'Moná Quintana',
    'edad':20,
    'estatura':1.65,
    'profesion':'Desarrollador de Software',
    'novia':'Ebony Alzate'
}
print(diccionario)
# Accediendo de forma individual a los atributos y valores de un diccionario

print(diccionario.get('nombre'))
print(diccionario['nombre'])

# Acceduebdi a Todos los atributos y valores de un diccionario al mismo tiempo

for clave,valor in diccionario.items():
    print(clave,':',valor)
    
    
