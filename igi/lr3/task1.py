import math
from CheckInput import check_int_float
def task_1():
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
        if dp < exp:
            break

    print(ans, math.asin(x), f'number of iterations: {kol}', sep='\n')