"""
Задача: написать функцию для сложения двух дробей, заданных числителями и знаменателями.

Результат работы функции (x, y) должен удовлетворять свойствам:
1. a/b + c/d = x/y
2. x/y несократима
3. y >= 0

Можно считать, что передаваемые в функцию b и d всегда ненулевые.
"""

"""
Функция сложения дробей a/b и c/d
Должна возвращать числитель и знаменатель дроби-результата
"""

def add_fractions(a, b, c, d):
    tempb, tempd = b, d
    NOD = b
    while tempb - tempd != 0:
        if tempb >= tempd:
            tempb, tempd = tempb - tempd, tempd
        else:
            tempd, tempb = tempd - tempb, tempb
        NOD = min(tempd, tempb)
    NOK = b * d / NOD
    x, y = a * NOK / b + c * NOK / d, NOK
    tempx, tempy = x, y
    NODxy = x
    while tempx - tempy != 0:
        if tempx >= tempy:
            tempx, tempy = tempx - tempy, tempy
        else:
            tempy, tempx = tempy - tempx, tempx
        NODxy = min(tempx, tempy)

    return int(x / NODxy), int(y / NODxy)

# Напишите тело функции и правильный return

