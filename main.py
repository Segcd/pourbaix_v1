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
ct = input("Coloque el valor de la concentración total: ")

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
    elementos_a_eliminar2 = []
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
            elementos_a_eliminar.append(elemento)
            break
        else:
            reactantes.append(elemento)
            elementos_a_eliminar.append(elemento)

    for elemento in elementos_a_eliminar:
        listado.remove(elemento)
    for elemento in listado:
        if elemento[0].isdigit():
            temp_2 = [elemento]*int(elemento[0])
            productos.extend(temp_2)
            elementos_a_eliminar2.append(elemento)
        elif elemento[:2].isdigit():
            temp_2_2 = [elemento]*int(elemento[:2])
            productos.extend(temp_2_2)
            elementos_a_eliminar2.append(elemento)
        else:
            productos.append(elemento)
            elementos_a_eliminar2.append(elemento)
    for elemento in elementos_a_eliminar2:
        listado.remove(elemento)

def cambiador():
    for idx, (elem1, elem2) in enumerate(zip(productos, reactantes)):
        if elem1[1:3] == elem2[1:3]:
            reactantes[idx] = ct
            productos[idx] = ct

colocador()
limpiador()
cambiador()


print(productos)
print(reactantes)