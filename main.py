import time
import os

# num1 = [123, 123123123123123] по 15
# num2 = [123123123]

def start():
    print("""
Выберите одно из действий:
\t1. Запустить вычисления
\t2. Считать текущее число
\t3. Записать стартовое число
\t4. Выйти из программы""")

def divide_(num):
    
    carry = 0
    res = []

    for n in num:
        tmp = (n + carry*(10**15)) // 2
        carry = (n + carry*(10**15)) % 2
        res.append(tmp)

    return res

def add_(num1, num2):
    
    dif = len(num1) - len(num2)
    carry = 0
    res = []

    for i in reversed(range(len(num1))):
        if i - dif >= 0:
            tmp = num1[i] + num2[i-dif] + carry
        else:
            tmp = num1[i] + carry

        if len(str(tmp)) > 15:
            carry = int(str(tmp)[:-15])
            tmp = int(str(tmp)[-15:])

        res.append(tmp)
    return list(reversed(res))

def multiply_(num):

    carry = 1
    res = []

    for n in reversed(num):
        tmp = n * 3 + carry

        if len(str(tmp)) > 15:
            carry = int(str(tmp)[:-15])
            tmp = int(str(tmp)[-15:])

        res.append(tmp)
    return list(reversed(res))

def read_(mode=0):
    
    if mode == 1:
        with open("number.txt", "r") as f:
            return f.read()

    with open("number.txt", "r") as f:
        num = f.read()
        res = []

        for i in range(len(num) //15 +1):
            res.append(int(num[-15:]))
            num = num[:-15]
        return list(reversed(res))

def write_(num, mode=0):

    if mode == 1:
        with open("number.txt", "w") as f:
            f.write(num)
        return 0

    with open("number.txt", "w") as f:
        res = ""
        for n in num:
            res += str(n)
        
        f.write(res)


def main(skip=5):

    # таймер
    timer = int(input("Введите время работы:\n\t(Для бесконечного цикла введите 0)\n"))
    start_time = round(time.time(), 3)

    # цикл загрузки
    while (round(time.time(), 3) - start_time) < timer if timer > 0 else 1:
        
        # считывание числа
        start_num = read_()

        # внутренний цикл
        for i in range(skip):
            os.system("clear||cls")
            
            # стартовые значения
            List = []
            steps = 0
            num = add_(start_num, [i])
            s_time = round(time.time(), 3)

            # расчёты
            while (num != [1]) and (num not in List):
                if num[-1] % 2 == 0:
                    num = divide_(num)
                else:
                    num = multiply_(num)

                steps += 1

                # проверка на продолжительность
                if (round(time.time(), 3) - s_time) > 60:
                    print("Alert!!")
            
            # вывод результатов числа
            else:
                print(f"Время всего: {round(time.time() - start_time, 3)}")
                print(f"Время на число: {round(time.time() - s_time, 3)}")
                print(f"\nШагов: {steps}")
                print(f"Проверенное число: {add_(start_num, [i])}")
        # запись числа
        else:
            write_(add_(start_num, [i+1]))
    
    # завершение общего цикла
    else:
        print("Completed")