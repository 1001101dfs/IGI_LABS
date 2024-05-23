def task_3():
    digits = "1234567890"
    letters = "уеыаоэяию"
    kol = 0

    print('The program counts the number of digits and vowel letters in the string')
    print('Input string')
    string = input()

    for i in string:
        if (i in digits) or (i in letters):
            kol += 1

    print(kol)
