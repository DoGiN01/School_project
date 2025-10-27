from os import system
import main

repeat = False
chunk = 15

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
        num = input("Введите число для проверки:\n\t")

        Lst = []
        while num:
            Lst.append(num[-chunk:])
            num = num[:-chunk]

        num = main.calc(Lst)
        print(f"Время на число: {num[0]}")
        print(f"\nШагов: {num[1]}")
        print(f"Проверенное число: {num[2]}")

    elif action == "3":
        system("clear||cls")
        print(main.read_(mode=1))
    
    elif action == "4":
        main.write_(input("Введите стартовое число:\n"), mode=1)
        system("clear||cls")
        print("Done")
    
    elif action == "5":
        exit(0)
    
    else:
        print("Неверный ввод! Повторите попытку")
