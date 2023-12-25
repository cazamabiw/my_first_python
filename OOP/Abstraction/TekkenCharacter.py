from abc import ABC, abstractmethod

# Abstract base class for Tekken character
class TekkenCharacter(ABC):
    def __init__(self, name, fighting_style, health):
        self.name = name
        self.fighting_style = fighting_style
        self.health = health

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

    def display_info(self):
        print(f"Name: {self.name}, Fighting Style: {self.fighting_style}, Health: {self.health}%")
