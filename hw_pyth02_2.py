'''
суть: принимаем на вход число N
и возвращаем список произведений чисел от 1 до N.
'''

def module (num):   # получаем модуль числа
    if (num == 0):
        return 0
    elif (num < 0):
        num = num*(-1)
    return num

ls = [1]
def fac (counter, locCount):
    global ls
#    locCount = 1
    if (locCount <= counter):
        ls.append (locCount * ls[-1])
        return fac(counter, locCount+1)
    else:
        return
try:
    def main (num):

        global ls
        if (num == 0):
            return 0
        elif (num < 0):
            return fac(module(num), 1)
        else:
            return fac(num, 1)
except:
    print("Что-то пошло не так")
def init ():
    print("Программа принимает на вход число N \n и возвращает список произведений чисел от 1 до N")
    try:
        num = int(input("Введите число \n"))
    except:
        print("Похоже, Вы ввели что-то, с чем эта манипуляция невозможна\n")
    main(num)
    ls.pop(0)
    print("Получился такой список: ", ls)
