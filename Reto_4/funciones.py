""" Módulo que contiene las funciones del reto 4 """

from pymongo import MongoClient

def consultar_empleado(cedula_empleado):
    """ funcion utilizada para borrar un empleado """
    try:
        client = MongoClient()
        client = MongoClient("mongodb://localhost:27017/")
        db_empleado = client['Empleados_cac']
        col_empleado = db_empleado['empleado']
        reg_cliente = col_empleado.find({"Cédula" : cedula_empleado})
        print(str(reg_cliente[0]))
        return reg_cliente[0]
                
    except IndexError:
        return -1

def insertar_empleado(empleado):
    """ funcion utilizada para insertar un empleado """
    try:
        client = MongoClient()
        client = MongoClient("mongodb://localhost:27017/")
        db_empleado = client['Empleados_cac']
        col_empleado = db_empleado['empleado']
        cliente_id = db_empleado.empleado.insert_one(empleado).inserted_id
        print(str(col_empleado.find_one({"_id": cliente_id})))

    except Exception as e:
        print("error" + str(e))

def borrar_empleado(cedula_empleado):
    """ funcion utilizada para borrar un empleado """
    try:
        client = MongoClient()
        client = MongoClient("mongodb://localhost:27017/")
        db_empleado = client['Empleados_cac']
        col_empleado = db_empleado['empleado']
        empleado = {"Cédula" : cedula_empleado}
        col_empleado.delete_one(empleado)
        print("El empleado con cédula " + cedula_empleado + " se borró correctamente.")

    except Exception as e:
        print("error" + str(e))

def actualizar_empleado(empleado):
    """ funcion utilizada para actualizar un empleado """
    try:
        client = MongoClient()
        client = MongoClient("mongodb://localhost:27017/")
        db_empleado = client['Empleados_cac']
        col_empleado = db_empleado['empleado']
        cedula_empleado = empleado["Cédula"]
        col_empleado.update_one({"Cédula" : cedula_empleado}, {"$set": empleado})
        print("El empleado con cédula " + cedula_empleado + " se actualizó correctamente.")

    except Exception as e:
        print("error" + str(e))

def ejecutar_opcion_1_3(opcion):
    """ función para ejecutar la opción 1 (Crear) y 3 (Actualizar) del menú principal """
    try:
        cedula = input("Cédula: ")
        if consultar_empleado(cedula) != -1 and opcion == 1:
            print("El empleado ya existe.")
        else:
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            correo = input("Correo electrónico: ")
            cargo = input("Cargo: ")
            valor_hora = int(input("Valor Hora: "))
            horas_trabajadas = int(input("Horas Trabajadas: "))
            salario = valor_hora * horas_trabajadas
            reg_empleado = {"Cédula" : cedula,
                            "Nombre" : nombre,
                            "Apellidos" : apellidos,
                            "Correo Electrónico" : correo,
                            "Cargo" : cargo,
                            "Valor Hora" : valor_hora,
                            "Horas Trabajadas" : horas_trabajadas,
                            "Salario" : salario
                            }
            if opcion == 1:
                insertar_empleado(reg_empleado)
            elif opcion == 3:
                actualizar_empleado(reg_empleado)

    except ValueError:
        print("Debe ingresar un número.")
   
def ejecutar_opcion_2():
    """ función para ejecutar la opción 2 (Consultar) del menú principal """
    print("Opción 2 - Consultar Empleado")
    cedula = input("Cédula: ")
    consultar_empleado(cedula)

def ejecutar_opcion_4():
    """ función para ejecutar la opción 4 (Borrar) del menú principal """
    print("Opción 4 - Borrar Empleado")
    cedula = input("Cédula: ")
    borrar_empleado(cedula)
