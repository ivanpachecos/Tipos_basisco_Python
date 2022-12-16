#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

hora_trabajadas = int(input("Ingrese las horas trabajadas: "))
coste_por_horas = float(input("Ingrese el coste de horas: "))

total = hora_trabajadas * coste_por_horas
print("La paga sería de: " + str(total) + "$")