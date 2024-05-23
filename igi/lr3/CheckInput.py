import random
import time
from decimal import Decimal

def take_rand():
    return random.randint(0, 100000)

def check_int_input():
    while True:
        print('Input integer number')
        try:
            val = int(input())
            return val
        except ValueError:
            print("That's not an int!")

def timing_decorator(func):
    def wrapper():
        start_time = time.time()
        dp = func()
        end_time = time.time()
        print(f"Функция {func.__name__} выполнялась {end_time - start_time:.2f} секунд")
        return dp
    return wrapper
@timing_decorator
def check_int_float():
    while True:
        print('Input float number')
        try:
            val = Decimal(input())
            return val
        except ValueError:
            print("That's not an float!")

def check_int_input_in_range(min, max):
    while True:
        print(f'Input integer number in range [{min}; {max}]')
        try:
            val = int(input())
            if val >= min and val <= max:
                return val
            else:
                print("Incorrect input")
        except ValueError:
            print("That's not an int!")

