from cProfile import run
from concurrent.futures.process import _ResultItem
import os
import re
from datetime import datetime
from datetime import date
import random

def limpiarPantalla():
    os.system("cls")

############################################### MENU ##########################################################
def MenuPrin():
    while True:
        limpiarPantalla()
        try:
            res_menuP = int(input("""
            Bienvenido a "Creativos"
         
            1.- Comprar entradas
            2.- Mostrar ubicaciones disponibles  
            3.- Ver listado de asistentes
            4.- Mostrar ganancias totales

            0.- Cerrar programa 
            
            
            Elija una opcion: """))
            
            if res_menuP <= 4: 
                opcion = res_menuP

                if opcion == 1:
                    comprarR()
                elif opcion == 2:
                    mostrar2()
                elif opcion == 3:
                    asistentes()
                elif opcion == 4:
                    informe_arreglo()
                elif opcion == 0:
                    limpiarPantalla()
                    input("""Gracias por su confianza en "Creativos".
                     Bryan Delgado. 
                     Fecha: 08-07-2022 """)
                    break   
        except:
            print()
            input("La opcion ingresada no es valida. Presione enter para continuar")
            print()
####################################### FIN MENU ################################################################

####################################### DATOS ###################################################################
class Producto:
  def __init__(self, nombre, precio,cantidad, ventas):
    self.nombre = nombre
    self.precio = precio
    self.cantidad = cantidad
    self.ventas = ventas
  

e1 = Producto("Platinium", 120000, 20, 0)
e2 = Producto("Gold", 80000, 30, 0)
e3 = Producto("Silver", 50000, 50, 0)

class Informe:
    def __init__(self, nombre, ganancia, ventas):
        self.nombre = nombre
        self.ganancia = ganancia
        self.ventas = ventas

i1 = Informe(e1.nombre, 0, 0)
i2 = Informe(e2.nombre, 0, 0)
i3 = Informe(e3.nombre, 0, 0)


# PERSONA
rut = [20354889]
nombre = ["Juan"]
entradas=[0]

# CINE
cine = [     "1  2  3  4  5  6  7  8  9  10"
            ,"11 12 13 14 15 16 17 18 19 20"
            ,"21 22 23 24 25 26 27 28 29 30"
            ,"31 32 33 34 35 36 37 38 39 40"
            ,"41 42 43 44 45 46 47 48 49 50"
            ,"51 52 53 54 55 56 57 58 59 60"
            ,"61 62 63 64 65 66 67 68 69 70"
            ,"71 72 73 74 75 76 77 78 79 80"
            ,"81 82 83 84 85 86 87 88 89 90"
            ,"91 92 93 94 95 96 97 98 99 100"]

################################################## FIN DATOS ###############################################################


################################################## Mostrar ubicaciones disponibles ##########################################

def mostrar2():
    limpiarPantalla()
    for x in range(len(cine)):
        print(cine[x])
    print()
    input("Presione enter para continuar. ")  

################################################## Fin Mostrar ubicaciones disponibles######################################


################################################## Comprar entradas #########################################################

def comprarR():
    while True:
        res = validaRut()
        for x in range(0,len(rut)):
            if res not in rut:
                rut.append(res)
                nombre.append(validaNDueño())
                cuComprar()
                return
            else:
                cuComprar()
                return

def cuComprar():
    while True:
        x = input("Cuantos asientos desea comprar (Maximo 3): ")
        if x.isnumeric() == True and int(x) <= 3:
            contador = 0
            while contador <= (2):         # Debe ser un numero mnenor al limite
                contador = contador + 1
                comprar()
            return
        else:
                print("Error")
            

def comprar():
    for x in range(len(cine)):
            print(cine[x]) 
    while True:
        print()
        res = input("Elija el asiento que desea comprar: ")
        if res.isnumeric() == True :          
            if int(res) not in entradas: 
                entradas.append(int(res))
                
                if int(res) >= 1 and int(res)<= 10:                   
                    cine[0] = cine[0].replace(res,'X')
                    e3.cantidad-=1  
                    i3.ventas += 1
                    i3.ganancia +=(1*e3.precio)
                   
                elif int(res) >= 11 and int(res)<= 20:
                    cine[1] = cine[1].replace(res,'XX')
                    e3.cantidad-=1  
                    i3.ventas += 1
                    i3.ganancia +=(1*e3.precio)
                    
                elif int(res) >= 21 and int(res)<= 50:
                    for x in  range(2,5):
                        cine[x] = cine[x].replace(res,'XX')
                    e2.cantidad-=1  
                    i2.ventas += 1
                    i2.ganancia +=(1*e2.precio)
                    
                elif int(res) >= 51 and int(res)<= 100:
                    for x in  range(5,10):
                        cine[x] = cine[x].replace(res,'XX')
                    e1.cantidad-=1  
                    i1.ventas += 1
                    i1.ganancia +=(1*e1.precio)
                
                else:
                    input("Asiento no encontrado")
                    
                print("Se ha comprado el asiento ",res)
                input()
                return cine
       
            else:
                    input("No está disponible")
        else:
            input("No es numerico")
                    
                    
################################################## Fin Comprar entradas #####################################################


############################################## REGISTRAR PERSONA ###########################################################
def Registrar():
    limpiarPantalla()
    print("Ingrese los datos del Cliente")
    print()
    rut.append(validaRut())
    nombre.append(validaNDueño()) # nombre dueño # vvalidaNDueño()
    #edad.append(validaEdad())
####################################### FIN REGISTRAR PERSONA ##############################################################


###################################################### Listado de personas ################################################# 

def asistentes():
    rut.sort()
    limpiarPantalla()
    print("                   N° de Asistente o Compradores: ",len(rut))
    print("     Asistentes")
    for x in range(0,len(rut)):
        print(f"""                  
                Run: {rut[x]}
                Nombre {nombre[x]}
                    """)
    print()
    input("Presione enter para continuar")
###################################################### Fin Listado de personas ################################################


###################################################### INFORME ###############################################################
def informe_arreglo():
    limpiarPantalla()             
    input(f"""
                Ingresos por venta de Asientos


        
        Nombre: {e1.nombre}
        Ventas: {i1.ventas}
        Ganancia: {i1.ganancia}

        Nombre: {e2.nombre}
        Ventas: {i2.ventas}
        Ganancia: {i2.ganancia}
        
        Nombre: {e3.nombre}
        Eventas: {i3.ventas}
        Ganancia: {i3.ganancia}

        Total Ganancia: {i1.ganancia+i2.ganancia+i3.ganancia}
        
        
        Presiona enter para devolverse.    
            """)


################################################### VALIDACIONES ############################################################

# RUT       
def validaRut():
    while True:
        vRut = input("Ingrese Rut: ")
        if vRut.isnumeric() == True:
            vRut = int(vRut)
            if vRut >= 5000000 and vRut <= 99999999:
                return int(vRut)
            else:
                print()
                print ("Debe ingresar un RUT entre 5000000 a 99999999.")
                print()           
        else:
                print()
                print ("Debe ingresar un RUT entre 5000000 a 99999999.")
                print()

# NOMBRE DUEÑO
def validaNDueño():
    while True:
        x = input("Ingrese el nombre: ")
        if len(x) >= 2 and len(x) <= 15 and x.isalpha() == True:          
            return x.capitalize()
        else:
            print()
            print("El nombre debe tener entre 2 y 15 caracteres, debe ser solo letras.")
            print()

#################################################  FIN VALIDACIONES ###############################################
MenuPrin()
