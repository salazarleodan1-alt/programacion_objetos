class animal:
    def sonido(self):
        pass

class vaca(animal):
    def sonido(self):
        return "muuuuuu"
    
class ternero(animal):
    def sonido(self):
        return "meeeee"

animales = [vaca(),ternero()]
for animal in animales:
    print(animal.sonido())