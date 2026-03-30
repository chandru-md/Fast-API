from Enemy import *

enemy = Enemy()

enemy.type_of_enemy = "Kavitha"
enemy.talk()
enemy.walk_forward()
enemy.attack()
print(f"{enemy.type_of_enemy} has {enemy.health_points} health points and can do attack of {enemy.attack_damage}")