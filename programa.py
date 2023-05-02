database ={'clave': 'valor'}
continuar = False

def postData(myDatabase):
    print("----INGRESAR----" )
    nombre = input("Ingrese el nombre: ")
    password = input("Ingrese el password: ")
    if nombre =="" or password =="" :
        print("no ha ingresado datos")
    else:
        myDatabase[nombre] = password

def getData(myDatabase):
    print("----CONSULTAR----" )
    for clave, valor in myDatabase.items():
        print(clave + " "+ valor )
    print("------------------" )

def logUser(myDatabase):
        print("----LOGIN----" )
        nombre = input("Ingrese el nombre: ")
        password = input("Ingrese el password: ")
        contrasena = myDatabase.get(nombre,"Usuario o Password incorrecto")
        if(contrasena == password):
            print("Login exitoso. Bienvenido "+nombre)
            return True
        else :
            print(contrasena)
            return False

def myPanel(myDatabase):
    print("-------MENU-------" )
    print("Elija la opción:")
    print("1-Ingresar datos")
    print("2-Consultar datos")
    print("3-Login")
    print("0-Salir")
    opcion = input()
    if opcion == "1":
        postData(myDatabase)
        return False
    elif opcion == "2":
        getData(myDatabase)
        return False
    elif opcion == "3":
        return logUser(myDatabase)
    elif opcion == "0":
        return True
    else:
        print("Opcion incorrecta")
        return False

def myProgram(panel): 
    while panel != True:
        panel = myPanel(database)
        
myProgram(continuar)
