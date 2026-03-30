"""
what is encapsulation?

it is  bundling of data

what public class attributes means?

(__) = double underscore makes hide the data from public


why use encapsulation??

helps keep related fields and methods together
makes our code cleaner and easier to read
provides more flexibility to our code
provides more reusability with our code
"""

class Enemy:

    #def __init__(self):
       # pass

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.type_of_enemy

    # def set_type_of_enemy(self):
    #     self.__type_of_enemy
    # Abstraction --- part
    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to flight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")