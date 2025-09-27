from colorama import Style
from os import system
import main

while True:
    main.start()
    action = input()
    if action == "0":
        print("Поздравляю! Ты нашёл самую бесполезную пасхалку!")
    if action == "1":
        main.main()
        stop = input("Продолжить?(Y/N;default:Y): ")
        if stop in ("N", "n", "No", "no"):
            print(Style.RESET_ALL, end="")
            exit(0)
    elif action == "2":
        main.read()
    elif action == "3":
        main.write()
    elif action == "4":
        system("cls||clear")
        print(bin(int(input("Введите число для преобразования:\n")))[2:])
    elif action == "5":
        print(Style.RESET_ALL, end="")
        exit(0)
    else:
        print("Неверный ввод! Повторите попытку")
