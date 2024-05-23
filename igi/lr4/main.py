from Task1 import task_1
from CheckInput import check_int_input_in_range
from Task3 import task_3


while True:
    print('Введите номер задания')
    number = check_int_input_in_range(1, 5)
    if number == 1:
        task_1()
    elif number == 3:
        task_3()
