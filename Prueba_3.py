import os
import re
from datetime import datetime
from datetime import date
import random

def limpiarPantalla():
    os.system("cls")

############################################### MENU ##########################################################
def textMenuPrincipal():
    while True:
        limpiarPantalla()
        try:
            res_menuP = int(input("""
            Bienvenido Auto Seguro
                    Menu
         
            1.- Cargar auto
            2.- Buscar   
            3.- Imprimir Certificado
            4.- Informe

            0.- Cerrar programa 
            
            
            Elija una opcion: """))

            if res_menuP <= 4: 
                opcion = res_menuP

                if opcion == 1:
                    cargarAuto()
                elif opcion == 2:
                    buscar()
                elif opcion == 3:
                    imprimirCertificado()
                elif opcion == 4:
                    informe_arreglo()
                elif opcion == 0:
                    limpiarPantalla()
                    input("""Gracias por su confianza en Auto Seguro.
                     Bryan Delgado. 
                     Version: nose 16.7 """)
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
  
precioC = [1500, 2000, 2500, 3000, 3500, 1700, 2300, 2700, 3300]
for i in range(1):
    random.choice(precioC)

e1 = Producto("Anotaciones Vigentes", random.choice(precioC), 10, 0)
e2 = Producto("Emision de contaminantes", random.choice(precioC),10 , 0)
e3 = Producto("Multas", random.choice(precioC), 15, 0)

class Informe:
    def __init__(self, nombre, ganancia, ventas):
        self.nombre = nombre
        self.ganancia = ganancia
        self.ventas = ventas

i1 = Informe(e1.nombre, 0, 0)
i2 = Informe(e2.nombre, 0, 0)
i3= Informe(e3.nombre, 0, 0)


# PERSONA
rut = [7777777]
nombre = ["Juan"]
correo = ["juanXXX@gmail.com"]
edad = [55]
sexo = ["Masculino"]

# AUTO : Tipo, patente, marca y precio, multas (monto y fecha), fecha de registro del vehículo y nombre del dueño.
tipo = []
patente = []
marca = []
precio = []
nMultas = []
mMulta = []
fMulta = []
fRegistro = []
nDueño = [] 

################################################## FIN DATOS ###############################################################


################################################## CARGAR AUTO #############################################################
def cargarAuto():
    limpiarPantalla()
    print("Ingrese los datos del Auto")
    print()
    patente.append(validaPatente())
    marca.append(validaMarca())
    tipo.append(validaTipo())
    precio.append(validaPrecio())
    nDueño.append(validaNDueño())

    x = input("¿Tienes multas?(S/N):")
    if x[0].upper() == "S" and len(x) <=2:
        nMultas.append(1)
        mMulta.append(validaMonto())
        fMulta.append(validaFechaM())
    elif x[0].upper() == "N" and len(x) <=2:
        nMultas.append("Sin multas")
        mMulta.append("Sin multas")
        fMulta.append("Sin multas")

    fRegistro.append(validaFechaR())
    input(f"""Fecha de Registro: {validaFechaR()}
    
    "Presione enter para continuar""")
################################################## FIN CARGAR AUTO #########################################################
    

############################################## REGISTRAR PERSONA ###########################################################
def Registrar():
    limpiarPantalla()
    print("Ingrese los datos del paciente")
    print()
    rut.append(validaRut())
    nombre.append(validaNDueño()) # nombre dueño # vvalidaNDueño()
    correo.append(validaCorreo())
    edad.append(validaEdad())
    sexo.append(validaSexo())
####################################### FIN REGISTRAR PERSONA ##############################################################


##################################################### BUSCAR  ##############################################################
def buscar():
    while True:
        limpiarPantalla()
        print("            Buscar auto")
        print()
        res = (input("            Ingrese Patente: "))
        for x in range(0,len(patente)):
            if res.upper() == patente[x]:
                print()
                print(f"""            Información Vehiculo

                Tipo: {tipo[x]}
                Patente: {patente[x]}
                Marca: {marca[x]}
                Precio: {precio[x]}
                Nombre del Dueño: {nDueño[x]}
                Fecha registro: {fRegistro[x]}
                Cantidad de multas: {nMultas[x]}  
                Monto total de multa: {mMulta[x]}
                Fecha de la ultima multa: {fMulta[x]}

                
                
                
                Presione enter para continuar.
                """)
                input()
                return
                
                    
        else:
            print()
            input("La opcion ingresada no es valida. Presione enter para continuar. ")
################################################### FIN BUSCAR  ##############################################################


################################################### IMPRIMIR CERTIFICADOS  ###################################################
def imprimirCertificado():
    while True:
        limpiarPantalla()
        print("            Bienvenido a Atencion al Cliente")
        print()
        res = (input("            Ingrese patente: "))
        for x in range(0,len(patente)):
                if res.upper() == patente[x]:
                    global pat
                    global nom
                    global mont
                    pat = patente[x]
                    nom = nDueño[x]
                    mont = mMulta[x]
                    menuP()
                    return
                #else:
                #    input("juan")                 
        else:
            print()
            input("La opcion ingresada no es valida. Presione enter para continuar.")

def menuP(): 
   while True:
        limpiarPantalla()
        print(f"            Patente: {pat}")
        print()
        medi = (input(f"""            Elija la opcion que desea pagar.
                        

        1.-{e1.nombre}               $ {e1.precio}
        2.-{e2.nombre}       $ {e2.precio}
        3.-{e3.nombre}          $ {mont}
                        
        0.-Salir
                        
        Ingrese opcion: """))
        if medi.isnumeric() == True:
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
                input("La opcion ingresada no es valida. Presione enter para continuar.")
        else:
            print()
            input("La opcion ingresada no es valida. Presione enter para continuar.")
############################################### FIN  MENU IMPRIMIR CERTIFICADOS #########################################                
                                             
################# Opciones  #################  

def op1():
    cant_op1 = 1
    print()
    print(f"""   Certificado de {e1.nombre}""")
    if cant_op1 < e1.cantidad:
        e1.cantidad-=cant_op1   
        i1.ventas += cant_op1
        i1.ganancia +=(cant_op1*e1.precio)
        print()
        input(f"   {nom} has pagado un valor de {e1.precio} por {e1.nombre} de la patente {pat}. Presione enter para continuar.""")

def op2():   
    cant_op2 = 1
    print()
    print(f"""   Certificados de {e2.nombre}""")
    if cant_op2 < e2.cantidad:
        e2.cantidad -= cant_op2
        i2.ventas +=cant_op2
        i2.ganancia += (cant_op2*e2.precio)
        print()
        input(f"{nom} has pagado un valor de {e2.precio} por {e2.nombre} de la patente {pat}. Presione enter para continuar.""") 
   
def op3():
    for x in range(0,len(patente)):
        if pat == patente[x]:
            if mMulta[x] != "Sin multas":
                cant_op3 = nMultas[x]
                print(f""" Debe pagar {nMultas[x]} {e3.nombre}. """)
                print()
                if cant_op3 < e3.cantidad:
                    e3.cantidad -= cant_op3
                    i3.ventas +=  cant_op3
                    i3.ganancia += (cant_op3*mMulta[x])
                    nMultas[x] = "Sin multas"
                    mMulta[x] = "Sin multas"
                    input(f" {nom} has pagado {cant_op3} {e3.nombre} siendo un total {i3.ganancia} de {pat}. Presione enter para continuar.")
                
                else:
                    print()
                    input(f"        La cantidad que debe pagar debe ser menor a {e3.cantidad}.")
            else:
                input(f"Esta patente {pat} no tiene multas. Presione enter para continuar.")


################################################### FIN IMPRIMIR CERTIFICADOS   ##############################################


###################################################### INFORME ###############################################################
def informe_arreglo():
    limpiarPantalla()
    print("                   N° autos registrados: ",len(patente))
    for x in range(0,len(patente)):  
        print(f"""
                Autos

            Patente: {patente[x]}
            Nombre del Dueño: {nDueño[x]}
            Marca: {marca[x]}
            Tipo: {tipo[x]}            
            Precio: {precio[x]}
            Fecha registro: {fRegistro[x]}
            Cantidad de multas: {nMultas[x]}  
            Monto total de multa: {mMulta[x]}
            Fecha de la ultima multa: {fMulta[x]}
                """)

                
    input(f"""
                Ingresos por certificados y multas

        Nombre: {e1.nombre}
        Ventas: {i1.ventas}
        Ganancia: {i1.ganancia}

        Nombre: {e2.nombre}
        Ventas: {i2.ventas}
        Ganancia: {i2.ganancia}
        
        Nombre: {e3.nombre}
        Eventas: {i3.ventas}
        Ganancia: {i3.ganancia}
        
        
        Presiona enter para devolverse.    
            """)
###################################################### FIN INFORME ###############################################################   

def multas():
    while True:
        multa= validaFechaM()
        mul = validaMonto()


################################################### VALIDACIONES ############################################################

# EDAD
def validaEdad():
    while True:
        vEdad = input("Edad: ")
        if vEdad.isnumeric() == True:
            vEdad = int(vEdad)
            if vEdad >= 17 and vEdad <= 122:          
                return vEdad
            else:
                print()
                print ("La edad debe ser mayor a 18 años Y menor a 122.")
                print()
        else:
                print()
                print ("La edad debe ser mayor a 18 años Y menor a 122.")
                print()

# CORREO
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

# SEXO
def validaSexo():
    while True:
        vSexo = input("Sexo (F/M): ")
        if vSexo[0].upper() == "F" and len(vSexo) <= 8:
            vSexo = "Femenino"
            return vSexo
        elif vSexo[0].upper() == "M" and len(vSexo) <= 9:
            vSexo = "Masculino"
            return vSexo
        else:
            print()
            print ("El registro del Sexo debe ser (F/M).")
            print()

# RUT       
def validaRut():
    while True:
        vRut = input("Rut: ")
        if vRut.isnumeric() == True:
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

# PATENTE
def validaPatente():
  while True:
    x = input('Ingrese la patente: ')
    if x not in patente:
            if len(x) == 6:
                let = x[0]+x[1]
                let.isalpha()
                if  x[4].isnumeric() == True and x[5].isnumeric() == True and let.isalpha() == True:
                    return x.upper()
                else:
                    input("Los primero 2 caracteres deben ser letras y los ultimos dos caracteres deben ser numero.")  
            else:
                print("La patente debe tener entre 6 caracteres. Ejemplo 'BBAA66','BB6633'.")
    else:
        input("No puede repetir una patente ya registrada. Presione enter para continuar.")

# MARCA
def validaMarca():
  while True:
    x = input('Escribe nombre de la Marca: ')
    if len(x) >= 2 and len(x) <= 15 and x.isalpha() == True:       
      return x.capitalize()
    else:
      print()
      print("El nombre de la marca debe tener entre 2 y 15 caracteres, debe ser solo letras.")
      print()

# TIPO
def validaTipo():
    while True:
        x = input('Escribe el tipo de vehiculo: ')
        if len(x) >= 4 and len(x) <= 15 and x.isalpha() == True:           
            return x.capitalize()
        else:
            print()
            print("El tipo vehiculo debe tener entre 4 y 15 caracteres, debe ser solo letras.")
            print()

# NOMBRE DUEÑO
def validaNDueño():
    while True:
        x = input('Escribe el nombre del dueño: ')
        if len(x) >= 3 and len(x) <= 15 and x.isalpha() == True:          
            return x.capitalize()
        else:
            print()
            print("El nombre del dueño debe tener entre 2 y 15 caracteres, debe ser solo letras.")
            print()

# PRECIO
def validaPrecio():
    while True:
        precio = input("Escriba el precio: ")
        if precio.isnumeric() == True:
            precio = int(precio)
            if precio  >= 5000000:
                return precio
            else:
                print()
                print("El precio del auto debe ser mayor a 5000000 (5 millones).")
                print()
        else:
            print()
            print("El precio del auto deben ser numeros y ser mayor a 5000000 (5 millones). ")
            print()

# MONTO
def validaMonto():
    while True:
        monto = input("Escriba el monto de la multa: ")
        if monto.isnumeric() == True:
            monto = int(monto)
            return monto
        else:
            print()
            print("Escriba el monto con numeros.")
            print()

# NUMERO DE MULTAS
def validaNMulta():
    while True:
        nMulta = input("Escriba la cantidad de multas: ")
        if nMulta.isnumeric() == True:
            nMulta = int(nMulta)
            return nMulta
        else:
            print()
            print("Escriba la cantidad de multas con numeros.")
            print()

#FECHA MULTA
def validaFechaM():
  while True:
      try:
          fecha = input("Ingresa fecha de la multa en formato YYYY-MM-DD. Ejemplo 2021-03-05: ")
          datetime.strptime(fecha, '%Y-%m-%d')
      
          return fecha
      except ValueError:
          print("Debe ingresar una fecha en el formato YYYY-MM-DD. Ejemplo 2021-03-05.")

# FECHA REGISTRO
def validaFechaR():
  today = date.today()
  return today
   
#################################################  FIN VALIDACIONES ###############################################
textMenuPrincipal()