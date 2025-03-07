#Entrada
monto=int(input("Ingrese monto total de la compra"))

if(monto <=50):
    print("No hay descuento")

elif(monto >=50 and monto <=100):
    print(f"Descuento 5%", monto * 0.05)

elif(monto >100):
    print(f"Descuento 10%",monto * 0.10)