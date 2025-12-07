class animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("esta  ladrando")

class perro(animal):
    def dormir(self):
        print(f"{self.nombre} esta dormido")

p = perro("capy")
p.ladrar()
p.dormir()