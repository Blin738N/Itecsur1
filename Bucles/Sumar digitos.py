
num = input("Ingresa un numero entero: ")

suma = 0

for digito in num:
    suma += int(digito)

print(f"La suma de los digitos de {num} es: {suma}")
