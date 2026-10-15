peso = float(input("Calcula el coste del equipaje:"))
importe=0
if peso <=10:
    importe=0

elif peso <=20:
    importe = 20

else:
    importe = 5

print("El coste total del equipaje es:", importe, "€")