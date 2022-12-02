from main import *

player = make_hero(name="Вася Питонов", inventory=["зелье"], hp_now=100)
start_fight(player)
print("после боя")
show_hero(player)
