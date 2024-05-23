from task1 import task_1
from task2 import task_2
from task3 import task_3
from task4 import task_4
from task5 import task_5
from CheckInput import check_int_input_in_range


while True:
    print(True + False)
    print('select a task number')
    task = check_int_input_in_range(1, 5)
    if task == 1:
        task_1()
    elif task == 2:
        task_2()
    elif task == 3:
        task_3()
    elif task == 4:
        task_4()
    else:
        task_5()

    print("If you want continue print 1 else 0")

    ok = check_int_input_in_range(0, 1)

    if ok == 0:
        break

