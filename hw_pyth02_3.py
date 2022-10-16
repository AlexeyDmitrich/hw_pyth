'''
Суть: принимаем две строки, 
определяем количество вхождений одной строки в другую. 
Нельзя юзать find или count.
'''

def intro():
    global lon
    global shor
    print("Программа принимает на вход длинную строку, затем короткую строку, \n и ищет число вхождений второй в первую. \n")
    lon = str(input("Введите длинную строку \n"))
    shor = str(input("Введите строку, которую будем искать\n"))

# пробую применить к строкам операции, 
# как если бы они были списками
# если не прокатит - попытаюсь преобразовать строку к списку

def searchInArr (longArray, shortArray):
    counter = 0
    for i in range(len(longArray)):
        # нашел фичу для выдергивания куска строки по индексу
        # не знаю, законно ли это, но явного запрета не было
        if ((longArray[i:(i+len(shortArray))]) == shortArray):
            counter += 1
    return counter

def init():
    try:
        intro()
    except:
        print("Ошибка в блоке инициализации")
    try:
        aInB = searchInArr(lon, shor)
    except:
        print("Где-то произошла ошибка")
    print("Искомая строка входит в исследуемую ", aInB, " раз")

#Okeeey...
# for i in lon:
#     print(lon[i:(i+len(shor))])
# print(shor)
#print(len(shor))
#print(lon[2:(2+len(shor))])
# for i in range (len(lon)):
#     print(lon[i:(i+len(shor))])
# print(shor)