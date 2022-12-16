#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
can_inver = float(input("Ingrese la cantidad: "))
interes = int(input("Interes anual: "))
year = int(input("Ingrese el numero de años: "))

print("La capital de inversión obtenida es: " , str(round(can_inver * (interes / 100 + 1) ** year, 2)))