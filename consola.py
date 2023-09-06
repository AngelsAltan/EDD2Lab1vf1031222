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
        nuevaFecha = input("nueva fecha de nacimiento: ")
        nuevaDireccion = input("nueva direccion: ")
        if (nuevaFecha != '') & (nuevaDireccion != ''):
            i = 0
            while i < len(lista):
                lista[i].fechaNacimiento = nuevaFecha
                lista[i].direccion = nuevaDireccion
                i = i + 1
        else:
            print("sin cambios")

    elif(menu == "b"):
        print("b. Patch dpi")
        dpi = input("dpi de la persona a hacer patch: ")
        lista = arbolAplicantes.busquedaDpi(dpi)
        nuevaFecha = input("nueva fecha de nacimiento: ")
        nuevaDireccion = input("nueva direccion: ")
        if (nuevaFecha != '') & (nuevaDireccion != ''):
            i = 0
            while i < len(lista):
                lista[i].fechaNacimiento = nuevaFecha
                lista[i].direccion = nuevaDireccion
                i = i + 1
        else:
            print("sin cambios")

    elif(menu == "c"):
        print("c. Buscar nombre")
        nombre = input("nombre de las personas a buscar: ")
        lista = arbolAplicantes.busquedaNombreRango(nombre)
        i = 0
        while i < len(lista):
            print("Nombre: " + lista[i].nombre)
            print("DPI: " + lista[i].dpi)
            print("Fecha de nacimiento: " + lista[i].fechaNacimiento)
            print("Direccion: " + lista[i].direccion)
            i = i + 1
        print(str(i) + ", resultados")

    elif(menu == "d"):
        print("d. Buscar dpi")
        dpi = input("dpi de la persona a buscar: ")
        lista = arbolAplicantes.busquedaDpi(dpi)
        i = 0
        while i < len(lista):
            print("Nombre: " + lista[i].nombre)
            print("DPI: " + lista[i].dpi)
            print("Fecha de nacimiento: " + lista[i].fechaNacimiento)
            print("Direccion: " + lista[i].direccion)
            i = i + 1

    elif(menu == "e"):
        print("e. Eliminar Nombre")
        nombre = input("nombre de las personas a eliminar: ")
        lista = arbolAplicantes.busquedaNombreRango(nombre)
        i = 0
        while i < len(lista):
            arbolAplicantes.eliminar(lista[i])
            i = i + 1
        print(str(i) + ", eliminados")

    elif(menu == "f"):
        print("f. Eliminar dpi")
        dpi = input("dpi de la persona a eliminar: ")
        lista = arbolAplicantes.busquedaDpi(dpi)
        i = 0
        while i < len(lista):
            arbolAplicantes.eliminar(lista[i])
            i = i + 1

    elif(menu == "g"):
        opciones = False

    else:
        print("Error. al ingresar la opcion")
