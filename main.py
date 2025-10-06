import time
import os


# Вид чисел в обработке
# num1 = ['0000000000000123', '123123123123123'] по 15 символов в блоке
# num2 = ['000000123123123']


# Главное меню
def start():
    print("""
========================================
Выберите одно из действий:
\t1. Запустить вычисления
\t2. Считать текущее число
\t3. Записать стартовое число
\t4. Выйти из программы""")

# Деление на 2
def divide_(num):
    
    carry = 0
    res = []

    for n in num:
        tmp = (int(n) + carry*(10**15)) // 2
        carry = (int(n) + carry*(10**15)) % 2
        
        if len(str(tmp)) <= 15:
            tmp = '0'*(15-len(str(tmp))) + str(tmp)

        if len(str(tmp)) > 15:
            carry = int(str(tmp)[:-15])
            tmp = str(tmp)[-15:]
            
            if len(str(tmp)) <= 15:
                tmp = '0'*(15-len(str(tmp))) + str(tmp)

        res.append(tmp)

    return res

# Сложение
def add_(num1, num2):
    
    dif = len(num1) - len(num2)
    carry = 0
    res = []

    for i in reversed(range(len(num1))):
        if i - dif >= 0:
            tmp = int(num1[i]) + int(num2[i-dif]) + carry
        else:
            tmp = int(num1[i]) + carry

        if len(str(tmp)) <= 15:
            carry = 0
            tmp = '0'*(15-len(str(tmp))) + str(tmp)

        if len(str(tmp)) > 15:
            carry = int(str(tmp)[:-15])
            tmp = str(tmp)[-15:]
            if len(str(tmp)) <= 15:
                tmp = '0'*(15-len(str(tmp))) + str(tmp)

        res.append(tmp)
    return list(reversed(res))

# Умножение на 3 с прибавлением 1
def multiply_(num):

    carry = 1
    res = []

    for n in reversed(num):
        tmp = int(n) * 3 + carry

        if len(str(tmp)) <= 15:
            carry = 0
            tmp = '0'*(15-len(str(tmp))) + str(tmp)

        if len(str(tmp)) > 15:
            carry = int(str(tmp)[:-15])
            tmp = str(tmp)[-15:]
            if len(str(tmp)) <= 15:
                tmp = '0'*(15-len(str(tmp))) + str(tmp)

        res.append(tmp)
    return list(reversed(res))

# Чтение числа из файла
def read_(mode=0):
    
    if mode == 1:
        with open("number.txt", "r") as f:
            return f.read()

    with open("number.txt", "r") as f:
        num = f.read().strip()
        res = []

        while num:
            res.append(num[-15:])
            num = num[:-15]
        return list(reversed(res))

# Запись числа в файл
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


# Главный цикл обработки
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
            flag = True

            # расчёты
            while (num != ['000000000000001']) and (num not in List):
                if int(num[-1]) % 2 == 0:
                    num = divide_(num)
                else:
                    num = multiply_(num)

                steps += 1
                
                while num[0] == '000000000000000':
                    num.pop(0)

                # проверка на продолжительность
                if ((round(time.time(), 3) - s_time) > 15) and flag:
                    print("Число слишком долго обрабатывается! Желательна ручная проверка!")
                    flag = False
            
            else:
                if num in List:
                    print(f"Я нашёл цикл!!!\nОно: {num}")
                    exit(0)

                # вывод результатов числа
                work_time = round(time.time() - start_time, 3)
                print(f"Время работы программы: {int(work_time // 60 // 60 // 24)}:{int((work_time // 60 // 60) % 24)}:{int((work_time // 60) % 60)}:{round(work_time % 60, 3)}")
                print(f"Время на число: {round(time.time() - s_time, 3)}")
                print(f"\nШагов: {steps}")
                print(f"Проверенное число: {''.join(add_(start_num, [i]))}")
        # запись числа
        else:
            write_(add_(start_num, [i+1]))
    
    # завершение общего цикла
    else:
        print("Completed")