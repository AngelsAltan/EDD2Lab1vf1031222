from arbolBinario import arbolBinario_
from aplicantes import aplicantes_
import csv
import json

arbolAplicantes = arbolBinario_()

with open('input.csv') as a:
    archivoCompleto = csv.reader(a, delimiter=";")
    for fila in archivoCompleto:
        aplicanteActual = aplicantes_.from_json(str(fila[1]))
        if fila[0] == "INSERT":
            arbolAplicantes.insertar(aplicanteActual)

        elif fila[0] == "PATCH":
            if (arbolAplicantes.buscar(aplicanteActual)!= False):
                aplicanteActualizar = arbolAplicantes.buscar(aplicanteActual)
                aplicanteActualizar.direccion = aplicanteActual.direccion
                aplicanteActualizar.fechaNacimiento = aplicanteActual.fechaNacimiento
                arbolAplicantes.eliminar(aplicanteActual)
                arbolAplicantes.insertar(aplicanteActualizar)

            else:
                print("No se encontro a la persona")
                
        elif fila[0] == "DELETE":
            arbolAplicantes.eliminar(aplicanteActual)

    print("Se cargo el archivo correctamente!")

opciones = True
while(opciones):
    print("MENU:")
    print("a. Patch Nombre")
    print("b. Patch dpi")
    print("c. Buscar nombre")
    print("d. Buscar dpi")
    print("e. Eliminar Nombre")
    print("f. Eliminar dpi")
    print("g. Salir")
    menu = input("Ingrese su opcion: ")

    if(menu == "a"):
        print("a. Patch Nombre")
        nombre = input("nombre de las personas a hacer patch: ")
        lista = arbolAplicantes.busquedaNombreRango(nombre)
        fecha = input("nueva fecha de nacimiento: ")
        direccion = input("nueva direccion: ")
        if (fecha != '') & (direccion != ''):
            i =0
            while i < len(lista):
                lista[i].datebirth = fecha
                lista[i].address = direccion
                i += 1
        else:
            print("sin cambios")

    elif(menu == "b"):
        print("b. Patch dpi")
        dpi = input("dpi de la persona a hacer patch: ")
        lista = arbolAplicantes.busquedaDpi(dpi)
        fecha = input("nueva fecha de nacimiento: ")
        direccion = input("nueva direccion: ")
        if (fecha != '') & (direccion != ''):
            i =0
            while i < len(lista):
                lista[i].datebirth = fecha
                lista[i].address = direccion
                i += 1
        else:
            print("sin cambios")

    elif(menu == "c"):
        print("c. Buscar nombre")


    elif(menu == "d"):
        print("d. Buscar dpi")


    elif(menu == "e"):
        print("e. Eliminar Nombre")


    elif(menu == "f"):
        print("f. Eliminar dpi")


    elif(menu == "g"):
        menu = False

    else:
        print("Error. al ingresar la opcion")
