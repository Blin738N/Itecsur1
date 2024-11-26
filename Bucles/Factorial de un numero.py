
#Solicitar al usuario un numero
num = int(input("Ingresa un numero para calcular su factorial: "))

#Iniciar la variable
factorial = 1

#Calcular el factorial
for i in range(1, num + 1):
    factorial *= i

#Mostrar el resultado
print(f"El factorial de {num} es: {factorial}")
