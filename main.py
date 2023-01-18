def calculator():
    operation_pxn = input('''
tem q digitar a operação matemática que você gostaria:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = float(input('insira o primeiro número: '))
    number_2 = float(input('insira o segundo número: '))

    if operation_pxn == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation_pxn == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation_pxn == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation_pxn == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você nn digitou um operador certo, execute o programa novamente.')

calculator()
