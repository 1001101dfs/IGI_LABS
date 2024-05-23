from CheckInput import check_int_input
def task_2():
    print('You enter integers into the progroup until you enter 18. The program will eventually find the sum of the last digits ')
    sum = 0
    while True:
        a = check_int_input()
        if a == 18:
            break
        else:
            sum += a % 10

    print(sum)
