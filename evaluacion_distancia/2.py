# Definimos la clase Animal
class Animal:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Animal.
        
        Args:
            nombre (str): El nombre del animal.
            edad (int): La edad del animal.
        """
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        """
        Método que hace un sonido genérico de animal.
        """
        print("El animal hace un sonido.")

# Definimos la clase Gato, que hereda de Animal y agrega un nuevo método
class Gato(Animal):
    def maullar(self):
        """
        Método que hace que el gato maúlle.
        """
        print("El gato está maullando.")

# Creamos un objeto de la clase Gato y llamamos a sus métodos
mi_gato = Gato("Mimi", 2)
print(mi_gato.nombre)
print(mi_gato.edad)
mi_gato.hacer_sonido()
mi_gato.maullar()


# En este ejemplo, creamos dos clases: Animal y Gato. La clase Gato hereda de la clase Animal y agrega un nuevo método llamado "maullar". Creamos un objeto de la clase Gato llamado "mi_gato" y llamamos a sus métodos "hacer_sonido" y "maullar".