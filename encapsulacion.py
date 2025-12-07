class potreo:
    def __init__(self, vacas):
        self._vacas = vacas

    def ingrear_vacas(self, numero_de_vacas ):
        self._vacas += numero_de_vacas

    def get_vacas(self):
        return self._vacas
    
granjero = potreo(60)
granjero.ingrear_vacas(10)

print(granjero.get_vacas())