from producto import producto
from os import system
import os

opcion =0   ; codigo=0  ; nombre="" ; marca=0   ; precio=0
lista_productos=[]

def menu():
    try:
        system("cls")
        print("--- MENU DE PRODUCTOS ---")
        print("1. Agregar producto\n2.Mostrar Productos\n3.Salir")
        opcion = int(input("\n -- Seleccione Opción --"))
        if opcion==1:
            agregar()
        elif opcion==2:
            mostrar()
        elif opcion==3:
            salir()
            os._exit(1)
        else:
            erroropcion()
    except:
        print("Error en opcion del menu")
        system("pause")

def agregar():
    system("cls")
    print("--- REGISTRO DE PRODUCTO N°", len(lista_productos)+1)
    while True: #Solicitud de 1er dato codigo de producto
        try:
            codigo= int(input("Ingrese Código: "))
            break
        except:
            print("Error en registro de codigo")
            system("pause")

    while True: #Solicitud de 2do dato codigo de producto
        try:
            nombre= str(input("Ingrese nombre de producto: "))
            break
        except:
            print("Error en registro de nombre")
            system("pause")

    while True: #Solicitud de 3er dato codigo de producto
        try: 
            marca= int(input("Digite nro de marca |1.Lider|2.Jumbo|3.Santa Isabel| : "))
            if marca<1 or marca>3:
                print("Error en nro de marca")
            else:
                break
        except:
            print("Error en registro de nombre")
            system("pause")

    while True: #Solicitud de 4to dato codigo de producto
        try:
            precio= int(input("Ingrese precio: "))
            break
        except:
            print("Error en registro de precio")
            system("pause")

    pro= producto() #Declara una instancia (objeto) de la clase producto para registrar

    pro.setcodigo(codigo) 
    pro.setNombre(nombre)
    pro.setMarca(marca)
    pro.setPrecio(precio)

    lista_productos.append(pro) #se llama el arreglo y le entregamos con append la instancia(objetos) que tiene

def mostrar():
    if len(lista_productos) == 0:
        print("\n No existen productos registrados\n")
        system("pause")
        menu()
    else:
        system("cls")
        for x in lista_productos:
            print("Codigo: ", x.getcodigo() )
            print("Nombre: ", x.getNombre() )
            print("Precio: ", x.getPrecio() )
            if x.getMarca() == 1:   print("Marca: Lider")
            elif x.getMarca() == 2:  print("Marca: Jumbo")
            elif x.getMarca()== 3: print("Marca: Santa Isabel")
            print("--------------------")
            system("pause")
            menu()

def salir():
    print("Ejercicio finalizado. . .")

def erroropcion():
    print("Opción inválida, debe ser entre 1 y 3")
    system("pause")
    return menu()

menu()