import main
from colorama import Style

while True:
    main.start()
    action = input()
    if action == "0":
        print("Поздравляю! Ты нашёл самую бесполезную пасхалку!")
    if action == "1":
        main.main()
        stop = input("Продолжить?(Y/N): ")
        if stop in ("N", "n", "No", "no"):
            print(Style.RESET_ALL, end="")
            exit(0)
    elif action == "2":
        main.read()
    elif action == "3":
        main.write()
    elif action == "4":
        print(Style.RESET_ALL, end="")
        exit(0)
    else:
        print("Неверный ввод! Повторите попытку")
