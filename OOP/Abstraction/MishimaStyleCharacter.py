from TekkenCharacter import TekkenCharacter
# Concrete class for Mishima Style character
class MishimaStyleCharacter(TekkenCharacter):
    def __init__(self, name, health):
        super().__init__(name, "Mishima Style", health)

    def attack(self):
        print(f"{self.name} performs a powerful Mishima-style punch!")

    def defend(self):
        print(f"{self.name} blocks the opponent's attack with Mishima-style defense.")
