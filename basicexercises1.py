"""""
print(f'Exercício 1\n')
num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))
print('\n')
if num1 > num2:
    print(f'O maior número é: %.2f' % num1)
elif num2 > num1:
    print(f'O maior número é: %.2f' % num2)
elif num1 == num2:
    print(f'Os dois números sao iguais.')
    
print(f'Exercício 2\n')
from math import sqrt
num = float(input("Insira um número: "))
if num >= 1:
    raiz = sqrt(num)
    print(f"A raiz quadrada de tal número será: %.2f" % raiz) 
if num <= 0:
    print(f"O número é inválido.")
    
print(f'Exercício 3\n')
from math import sqrt
num = float(input("Insira um número: "))
if num > 0:
    raiz = sqrt(num)
    print(f'A raiz quadrada do número é: %.2f' % raiz)
if num < 0:
    aoquadrado = (num ** 2)
    print(f'O número negativo ao quadrado será: %.2f' % aoquadrado)
print('\n')

print(f'Exercício 4\n')
from math import sqrt
num = float(input("Insira um número: "))
if num > 0:
    raiz = sqrt(num)
    print(f'A raiz quadrada é: %.2f' % raiz)
    aosquare = (num ** 2)
    print(f'O número ao quadrado é: %.2f' % aosquare)
    print('\n')
elif num <= 0:
    print('Inválido.\n')
    
print(f'Exercício 5\n')
num = int(input("Insira um número qualquer: "))
if (num % 2) == 0:
    print("{0} é par!".format(num))
else: 
    print("{0} é ímpar!".format(num))
print('\n')

print(f'Exercício 6\n')
num = int(input("Insira o primeiro número: "))
num1 = int(input("Insira o segundo número: "))
if num > num1:
    print('O maior número é: %.2f' % num)
elif num1 > num:
    print('O maior número é: %.2f' % num1)
print(f'\nDiferença entre os números!')
if num > num1:
    diferenca = (num - num1)
    print("A diferença entre tais números será: %.2f" % diferenca)
elif num1 > num:
    diferenca1 = (num1 - num)
    print("A diferença entre tais números será: %.2f" % diferenca1)
print('\n')
    
"""""
print(f'Exercício 7\n')
