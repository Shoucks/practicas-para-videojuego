class personaje:
    pass
# Ahi quedari la clase personaje vacia
nombre = input ("Escribe tu nombre: ")
class Persona:
    def __init__(self, nombre, edad): # Inicia su caracteristica principal
        self.nombre = nombre  # Atributo del objeto
        self.edad = edad      # Atributo del objeto
    def saludar(self):
        print(f"Hola, me llamo {self.nombre}.")

