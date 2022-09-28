import FIFO

def assembler1():
    print("Напишите код, который обменивает значения в регистрах RSI и RDX. Т. е. если перед выполнением вашего кода в регистре RSI хранится число 1, а в регистре RDX хранится число 2, то после выполнения кода в регистре RSI должно храниться число 2, а в регистре RDX число 1.")
    RSI = input("RSI: ")
    RDX = input("RDX: ")
    RCX = RSI

    RSI = RDX
    RDX = RCX

    print(f"RSI = {RSI}\nRDX = {RDX}")
    return main()

def assembler2():
    print("Сложите два числа в регистрах RSI и RDX, результат должен быть в регистре RSI.")
    RSI = int(input("RSI: "))
    RDX = int(input("RDX: "))
    RSI += RDX
    print(RSI)

    return main()

def assembler3():
    print("В регистре RSI вам дано целое число - градусы по шкале Фаренгейта. Напишите код, который получит в регистре RSI сответствующее значение по шкале Цельсия C")
    RSI = int(input("fahrenheit: "))
    RSI = (int((((RSI - 32) * 5) / 9) * 1 ) / 1)
    print(int(RSI))

    return main()

def assembler4():
    print("В регистрах RSI и RDX вам даны два числа, ваша задача поменять их местами, как и в одном из предыдущих заданий. Но добавляется условие, что все остальные регистры общего назначения должны остаться неизменными. Т. е. если вы используете какой-то регистр общего назначения кроме RSI и RDX, то вы должны сохранить и затем восстановить сохраненное значение регистра (ну или не пользоваться этими регистрами вовсе)")
    RSI = input("RSI: ")
    RDX = input("RDX: ")
    RCX = RSI

    RSI = RDX
    RDX = RCX

    del RCX
    print(f"RSI = {RSI}\nRDX = {RDX}")

    return main()

def assembler5():
    print("А теперь ваша задача написать функцию swap. Функция принимает на вход два указателя на 64-битные числа (в регистрах RDI и RSI) и должна обменять значения в памяти.")
    RDI = input("RDI: ")
    RSI = input("RSI: ")

    def swap(RDI, RSI):
        RCX = RDI

        RDI = RSI
        RSI = RCX
        print(f"RSI = {RSI}\nRDX = {RDI}")
        return main()

    swap(RDI=RDI, RSI=RSI)

def assembler6():
    print("Попробуйте по аналогии с примером в лекции написать функцию, возвращающую минимум из двух переданных ей аргументов. Аргументы (беззнаковые целые числа) передаются в регистрах RDI и RSI. Результат работы функции должен быть сохранен в регистре RAX.")

    def minimum():
        RDI = int(input("RDI: "))
        RSI = int(input("RSI: "))

        RAX = min(RDI, RSI)
        rdi_gt(RAX=RAX)

    def rdi_gt(RAX):
        print(f"RAX ---> {RAX}")

        return main()
    minimum()

def assembler7():
    print("Теперь более сложное задание. Вам требуется написать функцию pow, которая принимает на вход два беззнаковых числа X и P (в регистрах RDI и RSI соответственно) и возвращает значение X^P  в регистре RAX. Гарантируется, что X и P не могут быть равны 0 одновременно (по отдельности они все еще могут быть равны 0). Также гарантируется, что ответ помещается в 64 бита.")

    RDI = int(input("x: "))
    RSI = int(input("p: "))

    def ppow(RDI, RSI):
        RAX = pow(RDI, RSI)
        return RAX

    if not (RDI == 0 and RSI == 0):
        print(f"{RDI}^{RSI} = {ppow(RDI=RDI, RSI=RSI)}")
        return main()
    else:
        assembler7()

def fifo():
    FIFO.main_FIFO()
    return main()

def main():
    print("\n[-------------]")
    for i in range(1, 8):
        print(f"{[i]} Assembler-{i}")
    print("[8] FIFO")

    choice = int(input("\n[*] Choice: "))

    if choice == 1:
        assembler1()
    elif choice == 2:
        assembler2()
    elif choice == 3:
        assembler3()
    elif choice == 4:
        assembler4()
    elif choice == 5:
        assembler5()
    elif choice == 6:
        assembler6()
    elif choice == 7:
        assembler7()
    elif choice == 8:
        fifo()
    else:
        print("[ERROR]")
        main()

if __name__ == '__main__':
    print('\n')
    print('''          _____             _ _          _   
         / ____|           (_) |        | |  
        | |  __  __ _ _ __  _| |__   ___| |_ 
        | | |_ |/ _` | '_ \| | '_ \ / _ \ __|
        | |__| | (_| | | | | | |_) |  __/ |_ 
         \_____|\__,_|_| |_|_|_.__/ \___|\__|

    ''')
    main()


