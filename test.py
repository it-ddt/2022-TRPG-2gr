from main import *

player = make_hero(
    name="Вася Питонов",
    hp_now=100,
    money=1000,
    inventory=[
        {
            "тип": "оружие",
            "название": "Меч-голова-с-плеч",
            "модификатор": 5,
            "цена": 500,
        }
    ],
)

game = True
while game:
    visit_hub(player)
