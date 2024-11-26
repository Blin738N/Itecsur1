
#Contraseña fija
clave_secreta= "secreto789"

#solicitar la contraseña al usuario
entrada_clave= input("Introduce la contraseña para el segundo acceso: ")

#Validar si la contraseña es correcta
if entrada_clave == clave_secreta:
    print("Acceso concedido")
else:
    print("Contraseña incorrecta")
    
