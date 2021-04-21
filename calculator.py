def add(num1, num2): 
    return num1 + num2
def minus(num1, num2):
    return num1 - num2
def division(num1, num2):
    return num1 / num2
def multiplication(num1, num2):
    return num1 * num2
class Calculator:
    print('Simple Calculator.')
    number_1 = int(input('Enter first number: '))
    number_2 = int(input('Enter second number: '))
    op = input('Enter Operation: ')
    if op == '+': print(number_1, '+', number_2, '=', add(number_1, number_2))
    elif op == '-': print(number_1, '-', number_2, '=', minus(number_1, number_2))
    elif op == '/': print(number_1, '/', number_2, '=', division(number_1, number_2))
    elif op == '*': print(number_1, '*', number_2, '=', add(number_1, number_2))
    else: print('There is not operation like that')
