"""
Задача: написать функцию для сложения двух дробей, заданных числителями и знаменателями.

Результат работы функции (x, y) должен удовлетворять свойствам:
1. a/b + c/d = x/y
2. x/y несократима
3. y >= 0

Можно считать, что передаваемые в функцию b и d всегда ненулевые.
"""
from math import lcm,gcd


def add_fractions(a, b, c, d):
    """
    Функция сложения дробей a/b и c/d
    Должна возвращать числитель и знаменатель дроби-результата
    """
    v1 = lcm(b,d)
    n1 = v1/b
    n2 = v1/d
    lower_number = int(v1)
    upper_number = int(a*n1+c*n2)
    v2 = gcd(upper_number,lower_number)
    upper_number = int(upper_number/v2)
    lower_number = int(lower_number/v2)
    return (upper_number,lower_number) # Напишите тело функции и правильный return