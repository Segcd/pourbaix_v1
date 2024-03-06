lista = ["Na2", "2Na", "para", "H2O", "3Cl", "12Mg"]

for elemento in lista:
    if elemento[0].isdigit() or elemento[:2].isdigit():
        print(elemento)
        lista.remove(elemento)
    elif elemento == "para":
        break

print(lista)

