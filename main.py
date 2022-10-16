




def switch ():

    print("\n ==================== МЕНЮ ===================")
    print(" |                                           |\n \
|  1. поиск суммы цифр числа                |\n \
|  2. задача похожая на поиск факториала    | \n \
|  3. подсчёт вхождений строки в др. строку |\n \
|  4. [в стадии разработки]                 |\n \
|  5. [в стадии разработки]                 |\n \
|  0. Выход                                 |\n \
=============================================")
    print("*** Нет адекватной реакции на повторный вызов ***")
    try:
        case = int(input("Выберите пункт меню.\n"))
    except:
        print("Нет, вводить нужно целое число.\n")
        switch()
    if (case == 2):
        import hw_pyth02_2
        hw_pyth02_2.init()
        switch()
        return
    elif (case == 1):
        import hw_pyth02_1
        hw_pyth02_1.init()
        switch()
        return
    elif (case == 3):
        import hw_pyth02_3
        hw_pyth02_3.init()
        switch()
        return
    elif (case == 0):
        print("Завершение работы программы")
        return
    else:
        print("Такого пункта меню пока нет(")
        switch()
        return

try:
    switch()
except:
    print("Соррян, произошла непредвиденная ситуация.")

