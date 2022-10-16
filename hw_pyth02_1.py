#Суть: принимаем на вход вещественное или целое число и возвращаем сумму его цифр. 
#Через строку нельзя решать.


print(\
    " Программа предназначена для расчета суммы \n \
цифр вещественных и целых чисел. \n \
    ____________ВНИМАНИЕ!_______________________________\n \
    | При слишком большой дробной части возможны сбои  |\n \
    | в вычислениях, вызываемые проблемой деления чисел| \n \
    | с плавающей точкой.                              |\n \
    |__________________________________________________|")
try:
    number = float(input("Введите число\n"))
except:
    print("Это точно число?\n")

def module(num):   # получаем модуль числа
    if(num == 0):
        return 0
    elif(num < 0):
        num = num*(-1)
    return num

def toInt (flt):    # умножаем число на 10, пока не избавимся от дробной части
    if((flt % 1) == 0.0):
        return flt
    else:
        return toInt (flt*10)

#print(module(number))

#print("вход:\n")

specialCount = 10
result = 0
lost = int(toInt(module(number)))
#print(specialCount, "\n", lost, "\n", result, "\n")

#print("обработка:\n")

def calcNums (number):  # считаем сумму цифр:
    num = number % specialCount # получаем остаток от деления на 10
#    print (num)                # тем самым, получая последнюю цифру
    global result 
    result = result+num         # эту цифру прибавляем к результату
#    print(result)
    global lost
    lost = (lost // specialCount) # и убираем из числа с помощью целочисленного деления на 10
#    print (lost)

while (lost > 0):   # пока число имеет в себе цифры - повторяем манипуляцию
    calcNums(lost)

#print ("вывод:\n")

print("Сумма всех цифр числа (до и после точки): ", result, "\n")
