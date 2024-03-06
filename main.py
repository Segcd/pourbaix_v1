#Ecuación de nerest
"""
pe = pe° - (1/n)*log(red/ox)
"""
#Introducción de datos

#E_est = float(input("Coloque el valor del potencial estandar: "))
#pe_est = E_est/0.059

listado = []
reactantes = []
productos = []

def colocador():
    print("Escribe las componentes una por una de la reacción A + B -> C + D ")
    print("Para representar un estado de oxidación se separa por un espacio: O 2- ")
    print("Para representar una molecula de dos atomos se pone junto: O2 ")
    print("Para separar los terminos de cada lado use ->")
    cont = "si"
    while cont == "si":
        inicial = input("Ahora coloca termino por termino ")
        cont = input("Desea continuar? (si/no): ")
        listado.append(inicial)

def limpiador():
    elementos_a_eliminar = []
    for elemento in listado:
        if elemento[0].isdigit():
            temp = [elemento]*int(elemento[0])
            reactantes.extend(temp)
            elementos_a_eliminar.append(elemento)
        elif elemento[:2].isdigit():
            temp2 = [elemento]*int(elemento[:2])
            reactantes.extend(temp2)
            elementos_a_eliminar.append(elemento)
        elif elemento == "->":
            break
        else:
            reactantes.append(elemento)
    for elemento in elementos_a_eliminar:
        listado.remove(elemento)
    for elemento in listado:
        if elemento[0].isdigit() or elemento[:2].isdigit():
            productos.append(elemento)
    print(reactantes)
    print(productos)

colocador()
limpiador()