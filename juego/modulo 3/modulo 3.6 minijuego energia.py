print ("Expedicion")
print ("Tienes 50 de energia si llega a 0 mueres, cada dia baja 15 y descansar suma 30")

energia = 50
vivo = True

for dia in range(1, 6):
    print(f"\nDia {dia}")
    energia -= 15
    print("Energia: ", energia)
    


    if energia <= 0:
        print("Has muerto")
        vivo = False
        break

    accion = input("¿descansar o caminar? ")  
    if accion == "descansar":
        energia += 30
    else:
        energia += 0

if energia <= 0:
    print("Has muerto")
    vivo = False
elif vivo:
    print("Sobreviviste")  