
#Solicitar un numero al usuario
num = int(input("Ingresa un numero para ver su tabla de multiplicar: "))

#Mostrar la tabla de multiplicar de 1 al 10
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
