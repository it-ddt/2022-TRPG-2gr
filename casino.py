import os


def show(player):
    money = player[5]

    while True:

        # очищаем экран и показываем текст лавки
        os.system("cls")
        print(f"{player[0]} приехал в трактир. Трактирщик Харитон предлагает сыграть в кости на деньги.")

        # показываем персонажа
        print("имя:", player[0])
        print("жизни:", player[1])
        print("опыт", player[2])
        print("атака:", player[3])
        print("защита:", player[4])
        print("деньги:", player[5])
        print("зелья:", player[6])
        print("")

        # показываем варианты в лавке
        print("1 - Сыграть в кости")
        print("2 - Уехать обратно к камню")
        answer = input("\nВведите номер варианта и нажмите ENTER: ")
        if answer == "1":
            os.system("cls")
            if money >= 10:
                money -= 10
                potions += 1
                print("Купили зелье")
            else:
                print("Недостаточно монет!")
            input("\nНажмите ENTER чтобы продолжить")
        elif answer == "2":
            return (player[0], player[1], player[2], player[3], player[4], money, player[6])