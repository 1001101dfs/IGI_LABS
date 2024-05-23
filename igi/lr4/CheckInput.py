from datetime import datetime
from decimal import Decimal

def check_date_input():
    while True:
        try:
            string = input()
            datetime.strptime(string, "%d.%m.%Y")
            return string
        except ValueError:
            print("Неправильный формат ввода")

def check_int_input():
    while True:
        print('Input integer number')
        try:
            val = int(input())
            return val
        except ValueError:
            print("That's not an int!")


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

def check_int_float():
    while True:
        print('Input float number')
        try:
            val = Decimal(input())
            return val
        except ValueError:
            print("That's not an float!")