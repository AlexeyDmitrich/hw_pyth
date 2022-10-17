'''
Вторая версия меню (в разработке)
'''

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
    caseList = []
    try:
        case = int(input("Выберите пункт меню.\n"))
    except:
        print("Нет, вводить нужно целое число.\n")
        switch()
    caseList.append(case)

    if (caseList[0] == 2):
        import hw_pyth02_2
        hw_pyth02_2.init()
        caseList.pop(0)
        switch()
        return
    elif (caseList[0] == 1):
        import hw_pyth02_1
        hw_pyth02_1.init()
        caseList.pop(0)
        switch()
        return
    elif (caseList[0] == 3):
        import hw_pyth02_3
        hw_pyth02_3.init()
        caseList.pop(0)
        switch()
        return
    elif (caseList[0] == 0):
        print("Завершение работы программы")
        caseList.pop(0)
        return
    else:
        print("Такого пункта меню пока нет(")
        switch()
        return

try:
    switch()
except:
    print("Соррян, произошла непредвиденная ситуация.")