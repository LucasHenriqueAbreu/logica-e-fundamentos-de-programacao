def somar(num1, num2):
    return num1 + num2

def dividir(num1, num2):
    return num1 / num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def menu():
    num1 = int(input('Informe um número: '))
    num2 = int(input('Informe outro número: '))
    decisao = input('Informe qual operaçõe matemática deseja saber')

    if decisao == '+':
        print('Resultado da soma: ', somar(num1, num2))
    elif decisao == '*':
        print('Resultado da multi: ', multiplicar(num1, num2))
    elif decisao == '/':
        print('Resultado da divisão: ', dividir(num1, num2))
    elif decisao == '-':
        print('Resultado da subtração: ', subtrair(num1, num2))
    else:
        print('Oção inválida, seu apedeuta!')


menu()