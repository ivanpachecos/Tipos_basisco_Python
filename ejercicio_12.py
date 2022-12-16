"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total. 2.094"""

x = int(input("La cantidad de barras de pan que desea: "))
y = int(input("La cantidad de pan que no es de día: "))

print("==========================================================================")
cantidad_pan = (3.49 * x)
cantidad_no_dia = (2.094 * y)
total = cantidad_pan + cantidad_no_dia

print("El valor de barras de pan bueno es: ", str(round(cantidad_pan,2)),"\nEl valor de las barras de pan no fresco con el descunto  es de:", str(round(cantidad_no_dia,2)))
print("===========================================================================\nEl total a pagar es: ", str(round(total,2)), "$\n============================================================================")