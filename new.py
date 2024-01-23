def tabuada():
    for num1 in range(1, 11):
        print(f'\nTabuada do número: {num1}\n')
        for num2 in range(1, 11):
            print(f'{num1} X {num2} = {num1 * num2}')
tabuada()