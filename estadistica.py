datos = []
def ingreso_datos(datos):
    Ndatos = int(input("cuantos datos quiere ingresar "))
    contador1 = 0
    while Ndatos > contador1:
        dato = int(input(f"dame el dato #{contador1+1} "))
        datos.append(dato)
        contador1 += 1
    return datos

def ordenar(datos):
    datos.sort(reverse = True)
    return datos

while True:
    fin = input("escriba si para continuar, no para terminar ")
    if fin == "si" or fin == "Si" or fin == "SI" or fin == "sI":
        datos = ingreso_datos(datos)
    if fin == "no":
        break
    