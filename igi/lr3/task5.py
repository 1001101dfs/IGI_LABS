from CheckInput import check_int_input
from CheckInput import take_rand
from CheckInput import check_int_input_in_range

def task_5():
    print('In a list consisting of integer elements, calculate the modulo maximum element and the sum of the elements of the list up to the last even element')
    list = []
    print('for autocomplete data enter 1 otherwise 0')
    auto = check_int_input_in_range(0, 1)
    mx = -1
    for i in range(2):
        if auto == 0:
            list.append(check_int_input())
        else:
            list.append(take_rand())
        mx = max(mx, abs(list[i]))

    print(f'max modul {mx}')
    if list[2] % 2 == 0:
        print(list[0] + list[1])
    elif list[1] % 2 == 0:
        print(list[0])
    else:
        print(0)
    print(list)