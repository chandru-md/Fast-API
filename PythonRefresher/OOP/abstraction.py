"""
what is abstraction?

abstraction means to hide the implementation and only show necessary details to the user.

Why use abstraction?

This allows users to not have to understand what the functionality us behind scenes.

you can create simple and reusable code

it allows for a better use of the dry principle  (don't repeat yourself)

it enables python objects to become more scalable.
"""
class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    def talk(self):
        print("I am an enemy!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")


"""
enemy.talk()
enemy.walk_forward()
enemy.attack()
"""