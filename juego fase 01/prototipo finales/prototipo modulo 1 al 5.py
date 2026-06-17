inventario = [
    {
        "nombre": "Venda",
        "peso": 1,
        "valor": 5,
        "cantidad": 3,
        "cura": 25,
        "tipo": "Vida"
    },
    {
        "nombre": "Provisiones",
        "peso": 5,
        "valor": 3,
        "cantidad": 2,
        "cura": 50,
        "tipo": "nutrientes"
    },
    {
        "nombre": "Bebida energizante",
        "peso": 2,
        "valor": 1,
        "cantidad": 10,
        "cura": 30,
        "tipo": "energia"
    }
]
vida = 100
nutrientes = 100
energia = 100

print ("Juego comenzado")
print("\nDebes llegar al final de un camino para eso debes caminar 10 veces sin morir")
print("\nEmpiezas el juego con 3 Vendas, 2 Provisiones y 10 Bebidas energeticas")
print("\nCada vez que caminas sumas pierdes 15 de cada una de tus estadisticas y 15 de energia extra por dia, solo puedes caminar una vez por dia")

for decicion in range (1,5):
    decicion = input("\n¿Que quieres hacer? Inventario, Estado, Accion ")
    if decicion == "Inventario":
        for item in inventario:
            print("\ntienes", item["cantidad"], item["nombre"], "que cura", item["cura"], "de", item["tipo"], "cada uno")
    elif decicion == "Estado":
        print ("\nVida", vida,"/100")
        print ("Nutrientes", nutrientes,"/100")
        print ("Energia", energia,"/100")
