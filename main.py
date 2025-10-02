from bitarray import bitarray
from bitarray.util import ba2int
from colorama import Fore, Style, init
import time
import os
import pickle
init()


def divide(num):
    num = num[:-1]
    return num

def multiply_and_plus(num):
    tmp_num = num.copy()
    tmp_num.append(0)
    res = bitarray()
    c = 1

    for i in reversed(range(len(num))):
        j = int(num[i]) + int(tmp_num[i+1]) + c
        if j == 0:
            res.insert(0, 0)
            c = 0
        elif j == 1:
            res.insert(0, 1)
            c = 0
        elif j == 2:
            res.insert(0, 0)
            c = 1
        elif j == 3:
            res.insert(0, 1)
            c = 1
    else:
        if c == 0:
            res.insert(0, 1)
        else:
            res.insert(0, 0);res.insert(0, 1)

    return res

def add(num):
    c = 1
    res = bitarray()
    for i in reversed(num):
        j = i + c
        if j == 0:
            res.insert(0, 0)
            c = 0
        elif j == 1:
            res.insert(0, 1)
            c = 0
        elif j == 2:
            res.insert(0, 0)
            c = 1
    else:
        if c == 1:
            res.insert(0, 1)
    return res

def main():
    os.system("cls||clear")

    timer = int(input("Введите время работы программы в секундах:\n  (Для бессрочной работы введите 0)\n"))
    List = []
    n = bitarray()
    start_time = time.time()

    while (float(time.time()) - start_time) < timer if timer > 0 else 1:

        with open("number.bin", "rb") as f:
            num = pickle.load(f)
            n, n_s = bitarray(num), bitarray(num)
            del f, num
        
        for i in range(5):

            count = 0
            s_t = time.time()
            while (n.to01() != '1') and (not (n.to01() in List)):
                count += 1
                if (time.time() - s_t) > 30:
                    print("Внимание!!! Расчёт идёт слишком долго!!!\n  Может потребоваться ручная проверка")
                
                if n[-1] == 0:
                    n = divide(n)
                else:
                    n = multiply_and_plus(n)
            else:
                if n.to01() in List:
                    print(Style.RESET_ALL + Fore.BLUE + f"I found you! AHAHHAHAHAHAHAHAHHAHAHAHAHAHA!!!!!!!11!1!!\nYou are: {n_s}")
                    exit("d3d0c021")
            
            os.system("cls||clear")
            work_time = float(time.time()) - start_time
            print(Style.RESET_ALL + Fore.LIGHTGREEN_EX + f"Время работы программы: {int(work_time // 60 // 60 // 24)}:{int((work_time // 60 // 60) % 24)}:{int((work_time // 60) % 60)}:{round(work_time % 60, 3)}")
            print(Style.RESET_ALL + Fore.GREEN + f"Затраченное время: {round(time.time() - s_t, 3)}")
            print(Style.RESET_ALL + f"Шагов потребовалось: {count}")
            print(Style.RESET_ALL + Fore.RED + f"Число на проверке:\n\t(2)  {n_s.to01()}\n\t(10) {ba2int(n_s)}")

            n = add(n_s); n_s = add(n_s)
        
        with open("number.bin", "wb") as f:
            pickle.dump(n_s.to01(), f)
        del f, n, n_s

def read():
    with open("number.bin", "rb") as file:
        os.system("cls||clear")
        
        num = pickle.load(file)
        
        print(Style.RESET_ALL + Fore.RED + f"Текущее число:\n\t(2) {num}\n\t(10) {int(num, 2)}")

def write():
    with open("number.bin", "wb") as file:
        print(Style.RESET_ALL + Fore.RED + "Введите записываемое число:" + Style.RESET_ALL)
        
        num = bin(int(input()))[2:]
        
        pickle.dump(num, file)
        
        os.system("cls||clear")
        print(Style.RESET_ALL + "Запись прошла успешно!")

def start():
    print(Style.RESET_ALL + "\nВыберите одно из действий:")
    print("\t1. Запустить вычисления")
    print("\t2. Считать текущее число")
    print("\t3. Записать стартовое число")
    print("\t4. Выйти из программы")