from ast import Break
import os
from pickle import GLOBAL

def limpiarPantalla():
    os.system("cls")




########################################### MENU PRINCIPAL ######################################################
def textMenuPrincipal():
    while True:
        limpiarPantalla()
        try:
            res_menuP = int(input("""
                    Menu
            1.- Ingresar paciente
            2.- Atencion Paciente
            3.- Informe   

            0.- Cerrar programa 
            
            
            Elija una opcion: """))

            if res_menuP < 4: 
                opcion = res_menuP

                if opcion == 1:
                    Registrar()
                elif opcion == 2:
                    AtencionCliente()
                elif opcion == 3:
                    informe_arreglo()
                elif opcion == 0:
                    break
        
        except:
            print()
            input("La opcion ingresada no es valida. Presione enter para continuar")
            print()
          
####################################### FIN MENU PRINCIPAL ######################################################


####################################### DATOS ###################################################################
class Producto:
  def __init__(self, nombre, precio, cantidad, ventas):
    self.nombre = nombre
    self.precio = precio
    self.cantidad = cantidad
    self.ventas = ventas

e1 = Producto("Tapsin", 5000, 100, 0)
e2 = Producto("Agua de hierba", 15000, 250, 0)
e3 = Producto("Parecetamol", 3000, 75, 0)
            
class Informe:
    def __init__(self, nombre, ganancia, ventas):
        self.nombre = nombre
        self.ganancia = ganancia
        self.ventas = ventas

i1 = Informe(e1.nombre, 0, 0)
i2 = Informe(e2.nombre, 0, 0)
i3= Informe(e3.nombre, 0, 0)


#   DATOS

rut = [7777777]
nombre = ["Juan"]
correo = ["juanXXX@gmail.com"]
edad = [55]
sexo = ["Masculino"]
# registro = []
ps = ["Isapre"]
ob = ["Adicto al tusi"]



####################################### FIN DATOS ###############################################################


###################################### REGISTRAR ################################################################

def Registrar():
    limpiarPantalla()
    print("Ingrese los datos del paciente")
    rut.append(validaRut())
    nombre.append(input("Nombre: "))
    correo.append(validaCorreo())
    edad.append(validaEdad())
    sexo.append(validaSexo())
    ps.append(validaIF())
    ob.append(input("Observacion: "))


############################################## FIN REGISTRAR ###################################################


############################################## ATECENCION CLIENTE ##############################################

def AtencionCliente():
    while True:
        limpiarPantalla()
        print("            Bienvenido a Atencion al Cliente")
        print()
        res = (input("            Ingrese rut: "))
        if validaNumero(res) == True:
            res = int(res)
 
            for x in range(0,len(rut)):
                if res == rut[x]:
                    global nom
                    global obss
                    nom = nombre[x]
                    obss = ob[x]
                    menuP()
                    return
                #else:
                #    input("juan")
                    
        else:
            print()
            input("La opcion ingresada no es valida. Presione enter para continuar AAAAAA")


def menuP():
    while True:
        limpiarPantalla()
        print(f"            Nombre Paciente: {nom}")
        print(f"            Observacion: {obss}")
        print()
        medi = (input(f"""            Elija la opcion que desea comprar.
                        

        1.-{e1.nombre}               $ {e1.precio}
        2.-{e2.nombre}       $ {e2.precio}
        3.-{e3.nombre}          $ {e3.precio}
                        
        0.-Salir
                        
        Ingrese opcion: """))
        if validaNumero(medi) == True:
            medi = int(medi)
                        
            opcion = medi
            if opcion == 0:
                print()
                return
                                        
            elif opcion == 1:
                op1()
                                        
            elif opcion == 2:
                op2()
                                                            
            elif opcion == 3:
                op3()
                                    
            else:
                print()
                input("La opcion ingresada no es valida. Presione enter para continuar")
        else:
            print()
            input("La opcion ingresada no es valida. Presione enter para continuar")
############################################### FIN ATECENCION CLIENTE #########################################                
            
    
                    
                    
################################################# Opciones ########################################################      

def op1():
    cant_op1 = int(input(f"""
    Cuantas medicamentos de {e1.nombre} desea llevar: """))
    if cant_op1 < e1.cantidad:
        e1.cantidad-=cant_op1   
        i1.ventas += cant_op1
        i1.ganancia +=(cant_op1*e1.precio)
        print()
        input(f"    Ha Comprado {cant_op1} por un valor total de {i1.ganancia}. Presione enter para continuar")
    
        
    else:
        print()
        input(f"        La cantidad a comprar debe ser menor a {e1.cantidad}")
        

def op2():   
    cant_op2 = int(input(f"""
    Cuantas medicamentos de {e2.nombre} desea llevar: """))
    if cant_op2 < e2.cantidad:
        e2.cantidad -= cant_op2
        i2.ventas +=cant_op2
        i2.ganancia += (cant_op2*e2.precio)
        print()
        input(f"    Ha Comprado {cant_op2} por un valor total de {i2.ganancia}. Presione enter para continuar")
  
    else:
        print()
        input(f"        La cantidad a comprar debe ser menor a {e2.cantidad}")
           
def op3():
    cant_op3 = int(input(f"""
    Cuantas medicamentos de {e3.nombre} desea llevar: """))
    if cant_op3 < e3.cantidad:
        e3.cantidad -= cant_op3
        i3.ventas +=  cant_op3
        i3.ganancia += (cant_op3*e3.precio)
        print()
        input(f"    Ha Comprado {cant_op3} por un valor total de {i3.ganancia}. Presione enter para continuar")
      
    else:
        print()
        input(f"        La cantidad a comprar debe ser menor a {e3.cantidad}")
######################################## FIN OPCIONES ##########################################################                   


############################################### INFORME ########################################################

def informe_arreglo():
    limpiarPantalla()
    print("                Lista Pacientes   N° pacientes: ",len(rut))
    for x in range(0,len(rut)):
        print(f"""
        Rut: {rut[x]}
        Nombre: {nombre[x]}
        Correo: {correo[x]}
        Edad: {edad[x]}
        Sexo: {sexo[x]}
        Isapre o Fonasa: {ps[x]}
        Observacion: {ob[x]}  

        """)

    
    input(f"""
                Medicamentos Vendidos

        Nombre: {e1.nombre}
        Ventas: {i1.ventas}
        Ganancia: {i1.ganancia}

        Nombre: {e2.nombre}
        Ventas: {i2.ventas}
        Ganancia: {i2.ganancia}
        
        Nombre: {e3.nombre}
        Eventas: {i3.ventas}
        Ganancia: {i3.ganancia}
        
        
        Presiona enter para devolverse    
            """)
   
################################################### FIN INFORME ##################################################


################################################### VALIDACIONES ################################################
def validaEdad():
    while True:
        vEdad = input("Edad: ")
        if validaNumero(vEdad) == True:
            vEdad = int(vEdad)
            if vEdad >= 17 and vEdad <= 122: 
                vEdad = vEdad          
                return vEdad
            else:
                print()
                print ("La edad debe ser mayor a 18 años Y menor a 122.")
                print()
        else:
                print()
                print ("La edad debe ser mayor a 18 años Y menor a 122.")
                print()


def validaCorreo():
    while True:
        vCorreo = input("Correo: ")         
        if '@' not in vCorreo:
            print()
            print ("El correo debe contener el caracter @.")
            print()
            #return vCorreo
        else:
            return vCorreo

def validaSexo():
    while True:
        vSexo = input("Sexo (F/M): ")
        if vSexo == "F" or vSexo == "f":
            vSexo = "Femenino"
            return vSexo
        elif vSexo == "M" or vSexo == "m":
            vSexo = "Masculino"
            return vSexo
        else:
            print()
            print ("El registro del Sexo debe ser (F/M).")
            print()
        
def validaIF():
    while True:
        vIF = input("Isapre o Fonasa (I/F): ")
        if vIF == "I" or vIF == "i":
            vIF = "Isapre"   
            return vIF
        elif vIF == "F" or vIF == "f":
            vIF = "Fonasa"    
            return vIF
        else:
            print()
            print ("El registro del Isapre o Fonasa debe ser (I/F).")
            print()
        

def validaRut():
    while True:
        vRut = input("Rut: ")
        if validaNumero(vRut) == True:
            vRut = int(vRut)
            if vRut >= 5000000 and vRut <= 99999999:
                if vRut not in rut:
                        return int(vRut)
                else:
                    print("Este rut ya esta registrado.")
            else:
                print()
                print ("Debe ingresar un RUT entre 5000000 a 99999999.")
                print()           
        else:
                print()
                print ("Debe ingresar un RUT entre 5000000 a 99999999.")
                print()


def validaNumero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False


#################################################  FIN VALIDACIONES ###############################################

textMenuPrincipal()