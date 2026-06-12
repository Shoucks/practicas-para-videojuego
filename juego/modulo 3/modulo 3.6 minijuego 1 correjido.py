print ("Expedicion")
print ("Tienes 50 de energia si llega a 0 mueres, caminar baja 15 y descansar suma 30, diariamente igualmente pierdes 15 de energia")

energia = 50

for dia in range(1, 6):
    print(f"\nDia {dia}")
    energia -= 15
    print("Energia: ", energia)
    
    if energia <= 0:
        print("Has muerto")
        break

    accion = input("¿descansar o caminar? ")  
    if accion == "descansar":
        energia += 30
    elif accion == "caminar":
        energia -= 15
    else:
        energia += 0

    if energia <= 0:
        print("Has muerto")
        break

if energia >= 0:
    print("Sobreviviste")  