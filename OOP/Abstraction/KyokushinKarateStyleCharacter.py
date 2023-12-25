from TekkenCharacter import TekkenCharacter
# Concrete class for Kyokushin karate Style character
class KyokushinKarateStyleCharacter(TekkenCharacter):
    def __init__(self, name, health):
        super().__init__(name, "Kyokushin Karate Style", health)

    def attack(self):
        print(f"{self.name} performs a powerful Kyokushin-style axe kick!")

    def defend(self):
        print(f"{self.name} blocks the opponent's attack with Kyokushin-style defense.")
