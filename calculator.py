# Simple Calculator

from colored import fg
p = fg(162)
b = fg(80)
r = fg(9)
print(b+"\n-----------------------------------------------------------------------------\n")
print(b+"                   Simple Calculator\n                     For Learning.   \n                     By Tyizo, @1xm0d")
print(b+"\n-----------------------------------------------------------------------------\n")


def add(num1, num2):
    return num1 + num2

def subract(num1, num2):
    return num1 - num2

def multiplay(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print(b+'Operations:\n[+], [-], [*], [/]\r\n')

select = input(p+'Select One Operation Above ==> ')
number_1 = int(input(p+'Enter First Number ==> '))
number_2 = int(input(p+'Enter Second Number ==> '))

if select == '+':
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif select == '-':
    print(number_1, "-", number_2, "=", subract(number_1, number_2))
elif select == '*':
    print(number_1, "*", number_2, "=", multiplay(number_1, number_2))
elif select == '/':
    print(number_1, "/", number_2, "=", divide(number_1, number_2))

else:
    print(r+'Invalid Number\n')
    input(r+'Enter [exit] to exit my add:\n ')

