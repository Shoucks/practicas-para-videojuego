#muestra dia y anochecer dandole enter hasta que llega al final en el dia 3
dias_totales = 3
dia = 1

while dia <= dias_totales:
    print(f"Comienza el día {dia}")

    accion = input("Pulsa Enter para terminar el día...")

    print("Anochece")
    print("----------------")

    dia += 1

print("Fin de la simulación")