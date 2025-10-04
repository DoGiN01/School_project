from os import system
import main

repeat = False

while True:

    if not repeat:
        main.start()
        action = input()
    

    if action == "1":
        system("clear||cls")
        main.main()
        stop = input("Продолжить?(Y/N;default:N): ")
        if stop in ("Y", "y", "Yes", "yes"):
            repeat = True
        else:
            repeat = False
    
    elif action == "2":
        system("clear||cls")
        print(main.read_(mode=1))
    
    elif action == "3":
        main.write_(input("Введите стартовое число:\n"), mode=1)
        system("clear||cls")
        print("Done")
    
    elif action == "4":
        exit(0)
    
    else:
        print("Неверный ввод! Повторите попытку")
