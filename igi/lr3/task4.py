def task_4():
    print('The program does')
    print('a) find the number of words whose length is equal to 4 characters')
    print('b) find the words with the number of vowels equal to the number of consonants and their ordinal numbers consonants and their ordinal number')
    print('c) output the words in descending order of their lengths')
    string = input().split(' ')
    a_ans = 0
    b_ans = 0
    b_numbers = []
    vowel = 'уеыаоэяию'

    number_of_word = 0
    for i in string:

        if len(i) == 4:
            a_ans += 1

        kol = 0
        for j in i:
            if j in vowel:
                kol += 1

        if kol == len(i) - kol:
            b_ans += 1
            b_numbers.append(number_of_word)

        number_of_word += 1

    string.sort(key=len)
    print('a answer:', a_ans)
    print('b answer:', b_ans, b_numbers, sep='\n')
    print('c answer:', string, sep='\n')

