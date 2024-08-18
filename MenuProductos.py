"Menú básico de una pastelería en Python con inicio de sesión, listado de productos, estadísticas, registro de productos, precio total, etc..."
#Codificado por JotaDev // ¡Espero que te sirva!

#¡¡Linea [68] para editar nombre de usuario y contraseña!!

from os import system
import getpass
import os
global productos
productos=[]

# -------------------------------------------------------------------------------------------------------------------------------------------------|
def menu_inicial():    #-------------------aca debemos añadir el codigo correspondiente--------------------------
    
    #esta fx permite acceder a un menu de 2 opciones (1. iniciar sesion / 1. salir)
    try:
        system("cls")
        print("===== MENU PRINCIPAL PASTELERÍA =====")
        print(" 1.Iniciar sesión \n 2.Salir \n")
        opcion= int(input("Seleccione opción: "))
        if opcion==1:
            iniciar_sesion()
        elif opcion==2:
            salir()
            os._exit(1)
        else:
            print("ERROR: opción de menu principal incorrecta")
            system("pause")
            menu_inicial()
    except:
        print("ERROR: La opción seleccionada debe ser un nro entero.")
        system("pause")
        menu_inicial()

# -------------------------------------------------------------------------------------------------------------------------------------------------|
def iniciar_sesion():  #-------------------aca debemos añadir el codigo correspondiente-----------------------
        #validar y verificar el nombre y clave de usuario, luego las comprueba, si logra o no acceder deja un mensaje.
        
    system("cls")
    while True:         #-----SOLICITUD DE NOMBRE DE USUARIO-----
        try:
            print("\nIniciando sesión....\n")
            nom= str(input("digite su nombre de usuario: "))
            if len(nom.strip()) == 0:
                print("\nERROR: El nombre de usuario no puede quedar vacio.\n")
                system("pause")
            else:
                break
        except:
            print("ERRRO: error en ingreso de nombre de usuario.")
            system("pause")
            iniciar_sesion()

    while True:         #---SOLICITUD DE CLAVE DE USUARIO---
        try:
            print(f"Inicio de sesión para usuario: {nom.upper()}")
            con= getpass.getpass("Digite su contraseña de usuario: ")
            if len(con.strip()) == 0:
                print("\n ERROR: Clave de usuario no puede quedar vacia\n")
                system("pause")
            else:
                break
        except:
            print("\nERROR: error en ingreso de clave de usuario.\n")
            system("pause")
            
    #----- se comprueba que los datos de usuario corresponden a los registros del programa--------
    if nom=="admin" and con=="123":
        system("cls")
        print("\n Inicio de sesión correcto..\n")
        print(f"\n BIENVENIDO AL MENU DE ADMINISTRADOR {nom.upper()} \n")
        system("pause")
        menu_admin()        #si ingreso correctamente puede ir al menu admin
    else:
        system("cls")
        print("\n Usuario y/o Contraseña son incorrectos...\n")
        menu_inicial()
# -------------------------------------------------------------------------------------------------------------------------------------------------|
def cerrar_sesion():   #-------------------aca debemos añadir el codigo correspondiente------------------------
    while True:
        try:
            system("cls")
            opcion= int(input("¿Está seguro de cerrar la sesión de usuario? 1. SI // 2. NO :  "))
            if opcion==1:
                print("Cerrando sesión de usuario...")
                system("pause")
                menu_inicial()      #confirmando el ciere de sesion retorna al menu principal.
            elif opcion==2:
                menu_admin()        #si no confirma queda en el mismo menu del usuario admin.
            else:
                print("\nERROR: opcion de cierre de sesion incorrecto\n")
                system("pause")
        except:
            print("\nERROR: Opcion de cierre de sesion debe ser numérico.\n")
            system("pause")
            cerrar_sesion()
# -------------------------------------------------------------------------------------------------------------------------------------------------|
def menu_admin():      #-------------------aca debemos añadir el codigo correspondiente---------------------------
    try:
        system("cls")
        print("==== MENU DE USUARIO ADMIN ====")
        print("1.Registrar producto \n2.Ver Registros \n3.Estadistica \n4.Cerrar Sesión \n")
        opcion= int(input("Seleccione opcion: "))
        if opcion==1:   registrar_productos()
        elif opcion==2: listar_productos()
        elif opcion==3: estadistica()
        elif opcion==4: cerrar_sesion()
        else:
            print("ERROR: opcion de menu admin es incorrecta.")
            system("pause")
            menu_admin()
    except:
        print("ERROR: opcion de menu admin debe ser numerica")
        system("pause")
        menu_admin()
        
        
# -------------------------------------------------------------------------------------------------------------------------------------------------|
def registrar_productos():
    system("cls")
    print(f"==== REGISTRO DE PRODUCTO N°{len(productos) + 1} ====\n")
    while True: #------------------------------------------validacion y peticion del 1er dato--------------------------
        try:
            codigo= int(input("Ingrese codigo del producto: "))
            if codigo>=1:   break
            else:   print("Codigo debe ser >=1")
        except:     print("\n---ERROR: se esperaba un codigo solo de numeros ---")
    while True: #------------------------------------------validacion y peticion del 2do dato--------------------------
        try:
            nombre = str(input(f"Ingrese nombre del producto: "))
            if len(nombre) >=1:    break
            else:   print("\n--- El nombre no debe quedar vacio!! ---")
        except:     print("\n---ERROR: no se almaceno el nombre---")
    while True:  #------------------------------------------validacion y peticion del 3er dato--------------------------
        try:
            marca = int(input(f"Digite opcion de producto |1.Torta|2.Pastel|3.Coctel|: "))
            if marca>=1 and marca<=3:   break
            else:   print("\n---Marca incorrecta---", end="\n\n")
        except:     print("\n--- ERROR: se esperaba una marca como opcion numerica---")
    while True:  #------------------------------------------validacion y peticion del 4to dato--------------------------
        try:
            precio = int(input(f"Digite precio del producto: "))
            if precio>=500 and precio<=100000:  break
            else:   print("\n--- Precio debe estar entre $500 y $100000!!")
        except:     print("\n--- El Precio Debe Tener Solo Numeros!! ---")
    while True: #------------------------------------------validacion y peticion del 5to dato--------------------------
        try:
            cantidad = int(input(f"Digite cantidad: "))
            if cantidad>=1: break
            else: print("\n--- Cantidad debe ser >=1!!")
        except:     print("--- ERROR: se esperaba cantidad solo como numeros")
    #------------------------------------------------------calculo del 6to, 7mo, 8vo datos-----------------------------
    neto = precio*cantidad
    descuento = 0
    if marca==1:    descuento = neto*0.05
    elif marca==2:  descuento = neto*0.1
    elif marca==3:  descuento = neto*0.15
    total = neto-descuento
    productos.append([codigo, nombre, marca, precio, cantidad, neto, descuento, total])
    print(f"\n El registro del producto {nombre} se guardo correctamente \n")
    menu_admin()

# -------------------------------------------------------------------------------------------------------------------------------------------------|
def listar_productos():
    system("cls")
    if len(productos) == 0:
        print("--- No Hay Productos Para Listar!! ---")
        menu_admin()
    else:
        print("\n--- LISTADO DE PRODUCTOS ---")
        for contador, x in enumerate(productos):
            print(f"=== PRODUCTO N°{contador+1} ===")
            print(f"CODIGO   :   {x[0]}")
            print(f"NOMBRE   :   {x[1]}")
            if x[2] == 1: print("PRODUCTO :   Torta")
            elif x[2] == 2: print("PRODUCTO :   Pastel")
            else:   print("PRODUCTO :   Cóctel")
            print(f"PRECIO   : $ {x[3]}")
            print(f"CANTIDAD :   {x[4]}")
            print(f"NETO     : $ {x[5]}")
            print(f"DESCUENTO: $ {x[6]}")
            print(f"TOTAL    : $ {x[7]}")
            print("---------------------------")
        system("pause")
        menu_admin()

# -------------------------------------------------------------------------------------------------------------------------------------------------|
def estadistica():
    system("cls")
    ct=0; st=0; pt=0
    if len(productos)==0:
        print("--- No Hay Datos Para La Estadistica!! ---\n")
        system("pause")
        menu_admin()
    else:
        for x in productos:
            ct = ct+1       ;       st = st+x[7]
        pt = st/ct
        print("--- ESTADISTICA---")
        print(f"Suma De Totales     : ${st}")
        print(f"Promedio De Totales : ${pt}", end="\n\n")
        system("pause")
        menu_admin()

# -------------------------------------------------------------------------------------------------------------------------------------------------|
def salir():
    system("cls")
    print("-----------------------------")
    print("--- PROGRAMA FINALIZADO---")
    print("-----------------------------\n")
    system("pause")
# -------------------------------------------------------------------------------------------------------------------------------------------------|
	
menu_inicial()

#Codificado por JotaDev
#v1.0