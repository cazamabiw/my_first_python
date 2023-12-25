from MishimaStyleCharacter import MishimaStyleCharacter
from TaekwondoStyleCharacter import TaekwondoStyleCharacter
from KyokushinKarateStyleCharacter import KyokushinKarateStyleCharacter

mishima_character = MishimaStyleCharacter("Kazuya Mishima", health=80)
taekwondo_character = TaekwondoStyleCharacter("Hwoarang", health=90)
kyokushin_character = KyokushinKarateStyleCharacter("Jin Kazama", health=100)

mishima_character.display_info()
mishima_character.attack()
mishima_character.defend()

print("\n")

taekwondo_character.display_info()
taekwondo_character.attack()
taekwondo_character.defend()

print("\n")

kyokushin_character.display_info()
kyokushin_character.attack()
kyokushin_character.defend()