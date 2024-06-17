datos=[["Nombre", "Apellido", "Cargo", "Sueldo Bruto"],
        [],
        [],
        [],
        []]
listaTrabajadores=[]
listaTrabajadores.append(datos)
while True:
    print("Buenos días, ingrese la opción que desea ")
    print("1.-Registrar un trabajador")
    print("2.-Listar trabajadores")
    print("3.-Mostar plantilla de sueldos")
    print("4.-Salir")
    opcion=int(input("Elija su opción"))
    if opcion==1:
        trabajador=input("Ingrese su nombre: ")
        listaTrabajadores.append(trabajador)
        apellidotrabajador=input("Ingrese su apellido: ")
        listaTrabajadores.append(apellidotrabajador)
        cargo=input("Ingrese su cargo: ")
        listaTrabajadores.append(cargo)
        sueldobruto=input("Ingrese su sueldo bruto: ") 
        listaTrabajadores.append(sueldobruto)   
    elif opcion==2:
        print (listaTrabajadores)    
