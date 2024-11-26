
#Solicitar los dos numeros y la operacion
num1= float(input("Ingrese el primer numero: "))
num2= float(input("Ingrese el segundo numero: "))
oper= input("Ingrese la operacion (+, -, *, /): ")

#Reealizar el calculo segun la operacion
if oper== "+":
    restd= num1 + num2
elif oper== "-":
    restd= num1 - num2
elif oper== "*":
    restd= num1 * num2
elif oper== "/":
    if num2 != 0:
        restd= num1 / num2
    else:
        restd= "Error: Division por cero no permitido."
else:
    restd= "Operacion no valida."

#Mostrar el resultado
print(f"restd: {restd}")
