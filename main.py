from logging import debug
from validaciones import Validar
from empleados import Empleado
from titulo import Helper
from departamento import Departamento
from cargo import Cargo
import os
import time
#Inico
helper = Helper()
lista = ["1) Cargo","2) Departamento","3) Empleados","4) Salir"]
opcion=""
while opcion != "4":
  os.system("cls")
  opcion = helper.menu(lista,"MENU FICHA PERSONAL")
  if opcion == "1":
    opc1=""
    while opc1 != "3":
      os.system("cls")
      opc1 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"MANTENIMENTO DE CARGOS")
      os.system("cls")
      if opc1 == "1":
        while True:
          nombre= input("Cargo: ")
          if len(nombre)>=1 and len(nombre)<=20:
            break
          else:
            print("La entrada de cargo es incorrecta! Vuelva a intentar...")
        car = Cargo(nombre)
        carg = car.registro()
        Cargo.cargos.append(carg)
        input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
      elif opc1 == "2":
        print("*"*20,"LISTADO DE CARGOS","*"*20)
        print("Codigo"," "*5,"Descripcion")
        for carg in Cargo.cargos:
          cod = carg["codigo"]
          des=carg["cargo"]
          print(" "*2,cod," "*8,des)
        input("Presione una tecla para continuar...")        
  elif opcion == "2":
    opc1=""
    while opc1 != "3":
      os.system("cls")
      opc1 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"MANTENIMENTO DE DEPARTAMENTOS")
      os.system("cls")
      if opc1 == "1":
        while True:
          nombre= input("Departamento: ")
          if len(nombre)>=5 and len(nombre)<=20:
            break
          else:
            print("La entrada de Departamento es incorrecta! Vuelva a intentar...")
        dep = Departamento(nombre)
        depa = dep.registro()
        Departamento.departamentos.append(depa)
        input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
      elif opc1 == "2":
        print("*"*20,"LISTADO DE DEPARTAMENTOS","*"*20)
        print("Codigo"," "*5,"Descripcion")
        for depa in Departamento.departamentos:
          cod = depa["codigo"]
          des=depa["departamento"]
          print(" "*2,cod," "*8,des)
        input("Presione una tecla para continuar...") 
  elif opcion == "3":
    opc1=""
    while opc1 != "3":
      os.system("cls")
      opc1 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"INGRESO DE EMPLEADOS")
      os.system("cls")
      if opc1 == "1":
        while True:
          os.system("cls")
          nombre= input("Nombre: ")
          if len(nombre)>=3 and len(nombre)<=20:
            break
          else:
            print("Error! Vuelva a intentar...")
            time.sleep(0.8)
        while True: #Validacion de cedula
          os.system("cls")
          cedula=input("cedula: ")
          cedul=Validar.validarCedula(cedula)
          if cedul==True:
            if len(cedula)==10:
              break
          else:  
            print("Solo debe ingresar digitos...")
            time.sleep(0.8)
        while True: #Validacion de cargo
          os.system("cls")
          cargo=input("cargo: ")
          ca=Validar.buscarcargo(cargo)
          if cargo==ca:
              break
        while True: #Validacion de departamento
            os.system("cls")
            depar=input("Departamento: ")
            de=Validar.buscardepartamento(depar)
            if depar==de:
              break
        os.system("cls")
        while True:
          os.system("cls")
          sueldo=input("Sueldo: ")
          su=Validar.validarSueldo(sueldo)
          if su==True:
                sueldo=float(sueldo)
                break
          else:
              print("Error... Vuelva a intentar")
              time.sleep(0.8)
        
        # Agregamos todos estos datos a la calse Empleado...
        nom=Empleado(nombre,cedula,cargo,depar,sueldo)
        nomb=nom.registro()
        Empleado.empleados.append(nomb)
        
        input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
      elif opc1 == "2":
        print("*"*35,"LISTADO DE EMPLEADOS","*"*35)
        print("Codigo"," "*5,"Nombre"," "*12,"Cedula"," "*8,"Cargo"," "*8,"Departamento"," "*4,"Sueldo")
        for emp in Empleado.empleados:
          cod = emp["codigo"]
          nom=emp["nombre"]
          ced=emp["cedula"]
          car=emp["cargo"]
          dep=emp["departamento"]
          suel=emp["sueldo"]
          print(" "*2,cod," "*8,nom," "*(15-len(nom)),ced," "*(15-len(ced)),car," "*(15-len(car)),dep," "*(15-len(dep)),'$',suel)
        print("*"*92)
        input("\nPresione una tecla para continuar...") 

os.system("cls")        
print('*'*20,"Gracias por visitarnos",'*'*20)  


