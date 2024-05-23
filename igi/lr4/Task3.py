import math
from CheckInput import check_int_float
from Graph import Graph

def task_3():

    myClass = Graph()

    print('program counts asin through fourier series and outputs its value')
    from decimal import Decimal
    ans = Decimal(0.0)
    print('input x')
    x = Decimal(check_int_float())
    print('input exp')
    exp = Decimal(check_int_float())
    kol = 0
    for n in range(99):
        chislitel = Decimal(math.pow(x, 2 * n + 1)) * Decimal(math.factorial(2 * n))
        znam = Decimal(math.pow(4, n)) * Decimal(Decimal(math.pow(Decimal(math.factorial(n)), 2))) * Decimal(2 * n + 1)
        dp = chislitel / znam
        ans += dp
        kol += 1
        myClass.add_element(dp)
        if dp < exp:
            break

    print(f'среднее арифметическое элементов последовательности {myClass.sred_znach()}')
    print(f'медиана {myClass.median()}')
    print(f'мода {myClass.mode()}')
    print(f'дисперсия {myClass.variance()}')
    print(f'СКО  {myClass.standard_deviation()}')