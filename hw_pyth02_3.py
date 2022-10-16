'''
Суть: принимаем две строки, 
определяем количество вхождений одной строки в другую. 
Нельзя юзать find или count.
'''

lon = str(input("введите первую строку \n"))
shor = str(input("введите строку, которую будем искать\n"))

# пробую применить к строкам операции, 
# как если бы они были списками
# если не прокатит - недолго преобразовать строку к списку

def searchInArr (longArray, shortArray):
    counter = 0
    for i in range(len(longArray)):
        # нашел фичу для выдергивания куска строки по индексу
        # не знаю, законно ли это, но явного запрета не было
        if ((longArray[i:(i+len(shortArray))]) == shortArray):
            counter += 1
    return counter

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