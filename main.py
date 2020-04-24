# from  Player import player
#
# tim=player("Tim")
# print((tim.name))
# print(tim.lives)
# tim.lives -=1
# print(tim)
#
# tim.lives -=1
# print(tim)
#
# tim.lives -=1
# print(tim)

from enemy import Enemy, Troll, vampire

random_monster = Enemy("Basic Enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

ugly_troll = Troll("pug")
print("Ugly troll -{}".format(ugly_troll))

another_troll = Troll("UG")
print("Ugly troll -{}".format(another_troll))
another_troll.take_damage(18)
print(another_troll)

ugly_troll.grunt()
another_troll.grunt()
ugly_troll.grunt()

vamp = vampire("vall")
print(vamp)
vamp.take_damage(5)
print(vamp)

print("*" * 80)
another_troll.take_damage(80)
print(another_troll)

while vamp.alive:
    vamp.take_damage(1)
    print(vamp)
