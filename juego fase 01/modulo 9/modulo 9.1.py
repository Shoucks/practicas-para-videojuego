journal = []
while True:
    comando = input ("Salir / Continuar ")
    if comando == "Salir":
        break
    elif comando == "Continuar":
        while True:
            print ("Lib-lao esta comiendo")
            accion = input ("Observar / Nada ")
            if accion == "Observar":
                print ("Observas a Lib-lao hasta que deja de comer y parece buscar un lugar donde dormir")
                journal.append ("Observacion 1: Lib-lao se va a dormir luego de comer")
                print("\n--- JOURNAL ---")
                for entrada in journal:
                    print("*", entrada)
                break
            elif accion == "Nada":
                print("ves pasar el tiempo una hora")
            else:
                break
            print (journal)
        break
    else:
        print("Error de escritura")
#---------------------------------------------------------
while True:
    comando = input ("Salir / Continuar ")
    if comando == "Salir":
        break
    elif comando == "Continuar":
        while True:
            print ("Lib-lao esta durmiendo")
            accion = input ("Observar / Nada ")
            if accion == "Observar":
                print ("Observas a Lib-lao durmiendo durante una hora, al despertar defeca y sale corriendo")
                journal.append ("\nObservacion 2: Lib-lao defeca y sale corriendo luego de dormir")
                print("\n--- JOURNAL ---") 
                for entrada in journal:
                    print("*", entrada)
                break
            elif accion == "Nada":
                print("ves pasar el tiempo una hora")
            else:
                break
            print (journal)
        break
    else:
        print("Error de escritura")
#---------------------------------------------------------
while True:
    comando = input ("Salir / Continuar ")
    if comando == "Salir":
        break
    elif comando == "Continuar":
        while True:
            print ("Lib-lao está corriendo")
            accion = input ("Observar / Nada ")
            if accion == "Observar":
                print ("Observas a Lib-lao corriendo rapidamente junto a los de su especie buscando hierba, hasta que se queda sin energia y comienza a comer")
                journal.append ("\nObservacion 3: Lib-lao se pone a comer luego de correr durante una hora")
                print("\n--- JOURNAL ---") 
                for entrada in journal:
                    print("*", entrada)
                break
            elif accion == "Nada":
                print("ves pasar el tiempo una hora")
            else:
                break
            print (journal)
        break
    else:
        print("Error de escritura")
    
            