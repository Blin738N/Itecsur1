
#Defenir las credenciales
usuario= "admin"
contraseña= "1234"

#Intento permitidos
intento = 0

#Primer intento
usua= input("Ingrese el nombre de usuario: ")
contrasñ= input("Ingrese la contraseña: ")
    
if usua == usuario and contrasñ == contraseña:
    print(f"Bienvenido, {usuario}.")
else:
    intento += 1
    if intento < 3:
        print(f"Credenciales incorrectas. Intento {intento} de 3.")
        
        usua= input("Ingresa el nombre de usuario: ")
        contrasñ= input("Ingrese la contraseña: ")

        if usua == usuario and contrasñ == contraseña:
            print(f"Bienvenido, {usuario}.")
        else:
            print("Acceso bloqueado. has alcanzdo el numero maximo de intentos")
    else:
        print("Acceso bloqueado. Has alcanzado el numero de intentos.")
    
