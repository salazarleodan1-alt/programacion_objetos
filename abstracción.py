class Perro:
    def __init__(self, rasa, color):
        self.rasa = rasa
        self.color = color
        
    def Ladrar(self):
        print("Guau Guau")

mi_perro = Perro("Doberman", "cafe_claro")
mi_perro.Ladrar()