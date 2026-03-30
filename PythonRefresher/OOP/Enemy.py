class Enemy:

    #def __init__(self):
       # pass

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    # Abstraction --- part
    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to flight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")