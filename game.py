import os
import shop

def start_game():
    os.system("cls")
    print("Игра началась")

    # создаем игрока - КОРТЕЖ
    # [0] имя, [1] здоровье, [2] деньги, [3] зелья
    player = ("Вася Питонов", 100, 50, 0)

    # начался главный цикл игры
    while True:
        os.system("cls")

        # показываем персонажа
        print("Персонаж: ")
        print("имя:", player[0])
        print("здоровье:", player[1])
        print("деньги:", player[2])
        print("зелья:", player[3])
        print("")

        # показываем варианты
        print("1 - Поехать в лавку алхимика")
        print("0 - Выйти в главное меню")
        
        # выбираем вариант и проверяем его
        answer = input("\nВведите номер варианта и нажмите ENTER: ")
        if answer == "1":
            player = shop.show(player)

start_game()