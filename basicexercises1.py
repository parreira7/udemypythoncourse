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

print(f'Exercício 7\n')
num = float(input("Insira o primeiro número: "))
num1 = float(input("Insira o segundo número: "))
if num > num1:
    print('O maior número é: %.2f' % num)
elif num1 > num:
    print('O maior número é: %.2f' % num1)
elif num == num1:
    print(f'\nOs números sao iguais!\n')

print(f'Exercício 8\n')
nota = float(input('Insira a nota do primeiro aluno: '))
nota1 = float(input('Insira a nota do segundo aluno: '))
print('\n')
media = (nota + nota1) / 2
if nota and nota1 >= 0:
    print('A media será: %.2f' % media)
elif nota and nota1 < 0:
    print("Nota inválida.")
elif nota and nota1 > 10:
    print("Nota inválida!")

print(f'Exercício 9\n')
salario = float(input("Insira o salário mensal: "))
emprestimo = float(input("Insira o empréstimo desejado: "))
print('\n')
zero_ponto_2 = salario * 0.2
if emprestimo > zero_ponto_2:
    print("Empréstimo nao concedido!")
if emprestimo <= zero_ponto_2:
    print("Empréstimo concedido!")
    
print(f'Exercício 10\n')
sexo = input('Insira o sexo, sendo homem (H) e mulher (M): ')
altura = float(input("Insira a sua altura: "))
pesoH = (72.7 * altura) - 58
pesoM = (62.1 * altura) - 44.7
if sexo == "H":
    print("Seu peso ideal será: %.2f" % pesoH)
elif sexo == "M":
    print("Seu peso ideal será: %.2f" % pesoM)
else:
    print("Sexo inválido!")
print('\n')

print(f'Exercício 11\n')
num = int(input("Insira o número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\nAnalisando o número {}'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
soma = u + d + c + m
print('\nA soma dos digitos será: %.2f' % soma)

import math
print(f'Exercício 12\n')
num = int(input("Insira um número inteiro: "))
log = int(input("Informe o log de 'x': "))
if num <= 0:
    print(f'Número inválido.')
if num > 0:
    logaritmo = math.log(num, log)
    print("O número em forma logaritmica será: %.2f" % logaritmo)
    
print(f'Exercício 13\n')
def media_ponderada(x1, x2, x3, p1, p2, p3):
    mp1 = (x1 * p1) + (x2 * p2) + (x3 * p3)
    mp2 = p1 + p2 + p3
    resultado = mp1 / mp2
    return resultado

nota1, peso1 = float(input('Insira a nota do aluno na prova 1: ')), int(input("Insira o peso da nota 1: "))
nota2, peso2 = float(input('Insira a nota do aluno na prova 2: ')), int(input("Insira o peso da nota 2: "))
nota3, peso3 = float(input('Insira a nota do aluno na prova 3: ')), int(input("Insira o peso da nota 3: "))

media = media_ponderada(nota1, nota2, nota3, peso1, peso2, peso3)
print(f'\nA média será: %.2f' % media, '\n')

if media >= 6:
    print(f'O aluno foi aprovado!')
elif media <= 5 and media < 6:
    print(f'O aluno está em recuperaçao!')
elif media <= 4 and media < 5:
    print(f'O aluno está reprovado!')
print('\n')

print(f'Exercício 14 \n')
print(f'Dias da semana!')
num = int(input("\nInsira um número tendo(1) = domingo, a (7): "))
if num == 7:
    print(f'O número correspondente ao dia da semana será sábado!')
elif num == 6:
    print(f'O número correspondente ao dia da semana será sexta-feira!')
elif num == 5:
    print(f'O número correspondente ao dia da semana será quinta-feira!')
elif num == 4:
    print(f'O número correspondente ao dia da semana será quarta-feira!')
elif num == 3:
    print(f'O número correspondente ao dia da semana será terça-feira!')
elif num == 2:
    print(f'O número correspondente ao dia da semana será segunda-feira!')
elif num == 1:
    print(f'O número correspondente ao dia da semana será domingo!')
print('\n')

print(f'Exercício 15 \n')
print(f'Número correspondente à meses!')
num = int(input("Insira um número de 1 a 12: "))
if num <= 0:
    print(f'Número inválido!')
elif num > 12:
    print(f'Número inválido!')
elif num == 12:
    print(f'O número correspondente ao mes será dezembro!')
elif num == 11:
    print(f'O número correspondente ao mes será novembro!')
elif num == 10:
    print(f'O número correspondente ao mes será outubro!')
elif num == 9:
    print(f'O número correspondente ao mes será setembro!')
elif num == 8:
    print(f'O número correspondente ao mes será agosto!')
elif num == 7:
    print(f'O número correspondente ao mes será julho!')
elif num == 6:
    print(f'O número correspondente ao mes será junho!')
elif num == 5:
    print(f'O número correspondente ao mes será maio!')
elif num == 4:
    print(f'O número correspondente ao mes será abril!')
elif num == 3:
    print(f'O número correspondente ao mes será março!')
elif num == 2:
    print(f'O número correspondente ao mes será fevereiro!')
elif num == 1:
    print(f'O número correspondente ao mes será janeiro!')
    
print(f'Exercício 16')
print(f'Cálculo da área de um trapézio!')
def calculo(x1, x2, x3):
    area = (x1 + x2) * x3
    resultado = area / 2
    return resultado
base_maior = float(input("Insira a base maior do trapézio: "))
base_menor = float(input("Insira a base menor do trapézio: "))
altura = float(input('Insira a altura do trapézio: '))
if base_maior or base_menor or altura == 0:
    print(f'Número inválido!')
area_t = calculo(base_maior, base_menor, altura)
print(f'A área do trapézio será: %.2f' % area_t)    

print(f'Exercício 17')
#Se fosse necessário o cálculo dos lados, essa provavelmente seria a funçao:
#def calculo_area(x1, x2, x3):
#    calculo_lado = (x1 * x2 * x3) 
#    resultado = (calculo_lado) / 2
#    return resultado

ladoA = float(input("Insira o valor do lado(A): "))
ladoB = float(input("Insira o valor do lado(B): "))
ladoC = float(input("Insira o valor do lado(C): "))
if ladoA >= (ladoB + ladoC):
    print(f'Inválido, pois, o comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.')
elif ladoB >= (ladoA + ladoC):
    print(f'Inválido, pois, o comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.')
elif ladoC >= (ladoB + ladoA):
    print(f'Inválido, pois, o comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.')
elif ladoC >= (ladoA + ladoB):
    print(f'Inválido, pois, o comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.')    
elif ladoA == ladoB == ladoC:
    print(f'O triangulo é equilátero!')
elif ladoA == ladoB:
    print(f'O triangulo é isósceles!')
elif ladoA != ladoB != ladoC:
    print("O triangulo é escaleno!") 

print(f'Exercício 18')
pergunta = input('Insira a operaçao matemática: (adiçao), (subtraçao), (multiplicaçao), (divisao): ')
num1 = float(input('Insira o numero desejado: '))
num2 = float(input('Insira o numero desejado: '))
if pergunta == 'adiçao':
    soma = (num1 + num2)
    print(f'O resultado da soma dos números informados é = %.2f' % soma)
elif pergunta =='subtraçao':
    subtraçao = (num1 - num2)
    print(f'O resultado da subtraçao dos números é = %.2f' % subtraçao)
elif pergunta =='multiplicaçao':
    multiplicaçao = (num1 * num2)
    print(f'O resultado da multiplicaçao é = %.2f' % multiplicaçao)
elif pergunta == 'divisao':
    divisao = (num1 / num2)
    print(f'O resultado da divisao é = %.2f' % divisao)
""""
## {} []
