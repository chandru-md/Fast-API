from Enemy import *

enemy = Enemy("Sweety",2,55)
big_enemy = Enemy("kaushika",4,100)

enemy.talk()
enemy.walk_forward()
enemy.attack()
print(f"{enemy.type_of_enemy} has {enemy.health_points} health points and can do attack of {enemy.attack_damage}")