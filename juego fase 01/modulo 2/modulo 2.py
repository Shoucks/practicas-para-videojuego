#pide el valor de hambre para mostrar si tiene hambre o necesita comer o esta bien
hambre = int(input ("nivel de hambre de 0 a 100: "))
if hambre >= 70:
    print("necesitas comer")
elif hambre >= 30:
    print("tienes hambre")
else:
    print("estas bien")
