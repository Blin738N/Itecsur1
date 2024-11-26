
#Funcion que recibe el radio y retorne el area del circulo
def calcular_area(radio):
    pi = 3.1416
    return pi * radio ** 2

#Solicitar el radio al usuario
radio_ingresado = float(input("Introduce el radio del circulo: "))

#Llamar la funcion para calcular y mostrar el resultado
area = calcular_area(radio_ingresado)
print(f"El area del circulo con radio {radio_ingresado} es: {area:.2f}")
