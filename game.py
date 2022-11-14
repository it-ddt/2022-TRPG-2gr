import os
import shop
import hero_engine


def start_game():
    os.system("cls")
    print("Игра началась")

    # создаем игрока - КОРТЕЖ
    player = hero_engine.make_hero(name="Вася Питонов")


    # начался главный цикл игры
    while True:
        os.system("cls")

        # показываем персонажа
        hero_engine.show_hero(player)

        # показываем варианты
        print("1 - Поехать в лавку алхимика")
        print("0 - Выйти в главное меню")
        
        # выбираем вариант и проверяем его
        answer = input("\nВведите номер варианта и нажмите ENTER: ")
        if answer == "1":
            player = shop.show(player)
        elif answer == "2":
            print("едем в казино")


start_game()