contador = 1

while contador <= 5:
    print(contador)
    contador += 1 # Actualiza la condición

print()

print("¡Ciclo terminado!")
alumnos = ["Ana", "Luis", "Carlos"]

print()

for alumno in alumnos:
    print(f"Hola, {alumno}")

print()

    # Ejemplo con break
for numero in range(1, 10):
    if numero == 4:
        break  # Se detiene al llegar a 4
    print(numero)

print()

#slteando numeros
for numero in range(1, 11):
    if numero == 4:
        continue
    if numero == 5:
        continue
    if numero == 6:
        continue
    if numero == 7:
        continue
    elif numero == 11:
        break
    print(numero)

print()

#forma resumida del anterior
for numero in range(1, 11):
    if 4 <= numero <= 7:
        continue

    print(numero)