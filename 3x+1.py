from colorama import Style
from os import system
import main

repeat = False

while True:

    if not repeat:
        main.start()
        action = input()
    

    if action == "1":
        main.main()
        stop = input(Style.RESET_ALL + "Продолжить?(Y/N;default:N): ")
        if stop in ("Y", "y", "Yes", "yes"):
            repeat = True
        else:
            repeat = False
    
    elif action == "2":
        main.read()
    
    elif action == "3":
        main.write()
    
    elif action == "4":
        print(Style.RESET_ALL, end="")
        exit(0)
    
    else:
        print("Неверный ввод! Повторите попытку")
