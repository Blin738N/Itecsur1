
#Solicitar el monto de la compra

monto=float(input("Introduce el monto de la compra $"))

#Verficar si el monto es mayor a $100 para aplicar el descuento

if monto >100:
    desc= monto * 0.20 #20% de descuento
    mon_final= monto - desc
    print(f"Monto final ${mon_final:.2f}")
else:
    print(f"Monto final ${monto:.2f}")
