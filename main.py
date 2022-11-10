"""
TODO:
вынести создание и показ персонажа в модуль hero
игра в кости
сражение: атака, защита, пить зелье
инвентарь персонажа
ASCII-арт
"""

import os
import game


def main_menu():
    while True:
        os.system("cls")
        print("1 - начать новую игру")
        print("0 - выйти из игры")
        answer = input("\nВведите номер ответа и нажмите ENTER: ")
        if answer == "1":
            game.start_game()
        elif answer == "0":
            break


main_menu()
