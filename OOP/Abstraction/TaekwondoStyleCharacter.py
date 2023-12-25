from TekkenCharacter import TekkenCharacter
# Concrete class for Taekwondo Style character
class TaekwondoStyleCharacter(TekkenCharacter):
    def __init__(self, name, health):
        super().__init__(name, "Taekwondo Style", health)

    def attack(self):
        print(f"{self.name} executes a swift Taekwondo throw!")

    def defend(self):
        print(f"{self.name} uses Taekwondo techniques to counter the opponent's attack.")
