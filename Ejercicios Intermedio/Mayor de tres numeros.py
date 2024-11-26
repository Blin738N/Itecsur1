
#Solicitar tres numeros al usuario

num1= float(input("Introduce el primer numero"))
num2= float(input("Introduce el segundo numero"))
num3= float(input("Introduce el tercer numero"))

#Determinar cual es el numero mayor

if num1 >= num2 and num1 >= num3:
    prit("El numero mayor es: ", num1)
elif num2 >= num1 and num2 >= num3:
    print("El numero mayor es: ", num2)
else:
    print("El numero mayor es: ", num2)
