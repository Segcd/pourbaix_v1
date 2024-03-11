#Ecuación de nerest
"""
pe = pe° - (1/n)*log(red/ox)
"""
#Introducción de datos

#E_est = float(input("Coloque el valor del potencial estandar: "))
#pe_est = E_est/0.059

import matplotlib.pyplot as plt
import numpy as np

H = np.linspace(0, 1e-14, 100)
listado = []
reactantes = []
productos = []
ct = input("Coloque el valor de la concentración total: ")
pe_est = input("Coloque el valor del potencial estandar: ")

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
            multiplicador = int(elemento[0])
            temp = [elemento[1:]]*multiplicador
            reactantes.extend(temp)
            elementos_a_eliminar.append(elemento)
        elif elemento[:2].isdigit():
            multiplicador = int(elemento[:2])
            temp2 = [elemento[2:]]*multiplicador
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
            multiplicador = int(elemento[0])
            temp_2 = [elemento[1:]]*multiplicador
            productos.extend(temp_2)
            elementos_a_eliminar2.append(elemento)
        elif elemento[:2].isdigit():
            multiplicador = int(elemento[0])
            temp_2_2 = [elemento[1:]]*multiplicador
            productos.extend(temp_2_2)
            elementos_a_eliminar2.append(elemento)
        else:
            productos.append(elemento)
            elementos_a_eliminar2.append(elemento)
    for elemento in elementos_a_eliminar2:
        listado.remove(elemento)



colocador()
limpiador()

reactantes_bas=[]
productos_bas=[]

for elemento in reactantes:
    if elemento == "H":
        pass
    elif elemento == "e":
        pass
    elif elemento == ct:
        break
    else:
        reactantes_bas.append(elemento)
        reactantes.append(ct)

for elemento in reactantes_bas:
        reactantes.remove(elemento)    

for elemento in productos:
    if elemento == "H":
        pass
    elif elemento == "e":
        pass
    elif elemento == ct:
        break
    else:
        productos_bas.append(elemento)
        productos.append(ct)

for elemento in productos_bas:
        productos.remove(elemento)       


def convertir_lista(lista):
  nueva_lista = []
  for elemento in lista:
    try:
      nueva_lista.append(float(elemento))
    except ValueError:
      nueva_lista.append(elemento)
  return nueva_lista

reactantes_v2 = convertir_lista(reactantes)
productos_v2 = convertir_lista(productos)

print(reactantes_v2)
print(productos_v2)

reac_v2_bas =[]

for i in reactantes_v2:
    if i == "H":
        reac_v2_bas.append(i)
        reactantes_v2.append(H)