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
    
print(f'Exercício 19')
numero = int(input('Insira um numero.'))
def div3(numero):
    if numero % 3 == 0:
        return 'Divisível por 3'
        print(f'Divisível por 3.')
    elif numero % 3 != 0:
        print(f'por 3 será inválido.')

result = div3(numero)
print(result)

def div5(numero):
    if numero % 5 == 0:
        return 'Divisível por 5'
        print(f'Divisível por 5.')
    elif numero % 5 != 0:
        print(f'por 5 será inválido.')
        
result = div5(numero)
print(result)

print(f'Exercício 20')
pergunta = input('Insira a operaçao matemática: (adiçao), (diferença), (produto), (divisao): ')
num1 = float(input('Insira o número 1: '))
num2 = float(input('Insira o número 2: '))
if pergunta == 'adiçao':
    soma = (num1 + num2)
    print(f'O resultado da soma dos números informados é = %.2f' % soma)
elif pergunta == 'diferença':
    if num1 > num2:
        print(num1, f'será maior que', num2)
    elif num2 > num1:
        print(num2, f'será maior que', num1)
elif pergunta == 'produto':
    prod = (num1 * num2)
    print(f'O produto será %.2f' % prod)
elif pergunta == 'divisao':
    divisao = (num1 / num2)
    print(f'O resultado da divisao é = %.2f' % divisao)
else:
    print(f'Erro de digitaçao na pergunta.')
    
print(f'Exercício 21')
idade = int(input("Insira a idade: "))
tempotrab = int(input("Insira o tempo trabalhado durante a vida: "))
if (idade >= 65) and (tempotrab >= 30):
    print(f'Voce pode se aposentar.')
elif (idade >= 60) and (tempotrab >= 25):
    print(f'Voce pode se aposentar')
else:
    print(f'Voce nao pode se aposentar.')
    
print(f'Exercício 22')
ano = int(input("Insira um ano: "))
if (ano % 400 == 0) or (ano % 4 == 0) and (ano % 100 != 0):
    print(f'O ano é bissexto.')
else:
    print(f'Inválido. O ano nao é bissexto.')
    
print(f'Exercício 23')
mg = 0.07
sp = 0.12
rj = 0.15
ms = 0.08

valorP = float(input("Insira o valor da passagem: "))
destino = input("Insira o destino: (MG), (SP), (RJ) ou (MS): ")
if destino == 'MG':
    prod = (valorP * mg)
    soma = (prod + valorP)
    print(f'O preço da passagem será: %.2f' % soma)
elif destino == 'SP':
    prod = (valorP * sp)
    soma = (prod + valorP)
    print(f'O preço da passagem será: %.2f' % soma)
elif destino == 'RJ':
    prod = (valorP * rj)
    soma = (prod + valorP)
    print(f'O preço da passagem será: %.2f' % soma)
elif destino == 'MS':
    prod = (valorP * ms)
    soma = (prod + valorP)
    print(f'O preço da passagem será: %.2f' % soma)
else:
    print(f'Destino inválido.')
    
print(f'Exercício 24')
def bhaskara(x1, x2, x3):
    delta = (x2 ** 2) - 4 * (x1 * x3)
    calculox1 = (-x2 + delta ** (1 / 2)) / (2 * x1)
    calculox2 = (-x2 - delta ** (1 / 2)) / (2 * x1)
    if x1 == 0:
        print(f'O valor de A nao pode ser 0!')
    elif delta < 0:
        print(f'Nao existem raizes reais.')
    print(f'A raiz x1 será = %.2f' % calculox1)
    print(f'A raiz x2 será = %.2f' % calculox2)
    return calculox1
    return calculox2

valorA = float(input("Insira o valor de A: "))
valorB = float(input("Insira o valor de B: "))
valorC = float(input("Insira o valor de C: "))

calc = bhaskara(valorA, valorB, valorC)

print(f'Exercício 25')
distanciaKm = float(input("Insira a distancia percorrida em KM: "))
qtdLporP = float(input('Insira a quantidade de litros consumidas durante o percurso: '))
consumo = (distanciaKm / qtdLporP)
print(f'O consumo será de: %.2f' % consumo)
if (consumo) < 8:
    print(f'Venda o carro!')
elif (consumo >= 8) and (consumo <= 14):
    print(f'O carro é economico!')
elif (consumo > 12):
    print(f'O carro é super economico!') 
    
print(f'Exercício 26')
idade = float(input("Insira a idade: "))
if (idade >= 5) and (idade <= 7):
    print(f'Categorizado como infantil A')
elif (idade >= 8) and (idade <= 10):
    print(f'Categorizado como infantil B')
elif (idade >= 11) and (idade <= 13):
    print(f'Categorizado como juvenil A')
elif (idade >= 14) and (idade <= 17):
    print(f'Categorizado como juvenil B')
elif (idade >= 18):
    print(f'Categorizado como senior!')
    
print(f'Exercício 27')
pergunta = input("Qual funçao usará? (geométrica), (aritmética), (ponderada), (harmonica): ")
num1 = int(input("Insira o valor de x: "))
num2 = int(input("Insira o valor de y: "))
num3 = int(input("Insira o valor de z: "))
if (num1 <= 0) or (num2 <= 0) or (num3 <= 0):
    print(f'Inválido, os numeros devem ser positivos.')

elif pergunta == 'geométrica':
    calc = (num1 * num2 * num3)
    sqrt = calc ** (1./3.) 
    print(f'Usando a funçao geométrica o resultado será: %.2f' % sqrt)
elif pergunta == 'aritmética':
    calc = (num1 + num2 + num3) / 3
    print(f'Usando a aritmética teremos: %.2f como resultado' % calc)
elif pergunta == 'ponderada':
    peso = int(input("Insira o peso 1: "))
    peso1 = int(input("Insira o peso 2: "))
    calc = (num1 + peso * num2 + peso1 * num3)
    final = (calc) / (peso * peso1)
    print(f'A média ponderada será: %.2f' % final)
elif pergunta == 'harmonica':
    calc = 1 / ((1/num1) + (1/num2) + (1/num3))
    print(f'Utilizando da funçao harmonica teremos: %.2f como resultado' % calc)
else:
    print(f'Funçao da pergunta inválida.')
    
print(f'Exercício 28')
import random
num1 = random.randint(1, 101) 
num2 = random.randint(1, 101)
num3 = random.randint(1, 101)
num4 = random.randint(1, 101)
num5 = random.randint(1, 101)
num6 = random.randint(1, 101)
num7 = random.randint(1, 101)
num8 = random.randint(1, 101)
num9 = random.randint(1, 101)
num10 = random.randint(1, 101)
pergunta = [num1, num2]
nome = input("Insira o nome do aluno: ")
print(f'Faça a soma desses dois números: ', num1, num2)
resposta = int(input("Qual a resposta? R: "))
if resposta == (num1 + num2):
        print(f'Acertou!')
else:
    print('Errou')
        
print(f'Faça a soma desses dois números: ', num3, num4)
resposta = int(input("Qual a resposta? R: "))
if resposta == (num3 + num4):
    print(f'Acertou!')
else:
    print('Errou')
        
print(f'Faça a soma desses dois números: ', num5, num6)
resposta = int(input("Qual a resposta? R: "))
if resposta == (num5 + num6):
    print(f'Acertou!')
else:
    print('Errou')
    
print(f'Faça a soma desses dois números: ', num7, num8)
resposta = int(input("Qual a resposta? R: "))
if resposta == (num7 + num8):
    print(f'Acertou!')
else:
    print('Errou')
    
print(f'Faça a soma desses dois números: ', num9, num10)
resposta = int(input("Qual a resposta? R: "))
if resposta == (num9 + num10):
    print(f'Acertou!')
else:
    print('Errou')
    
print(f'Exercício 29')
num1 = int(input("Insira um número: "))
num2 = int(input("Insira um número: "))
num3 = int(input("Insira um número: "))
lista = [num1, num2, num3]
print(sorted(lista))

print(f'Exercício 30')
altura = float(input("Insira a altura: "))
peso = float(input("Insira o peso: "))
if (altura < 1.20) and (peso <= 60):
    print(f'Categoria A')
elif (altura < 1.20) and (peso >= 60) and (peso <= 90):
    print(f'Categoria D')
elif (altura < 1.20) and (peso > 90):
    print(f'Categoria G')
elif (altura >= 1.20) and (altura <= 1.70) and (peso <= 60):
    print(f'Categoria B')
elif (altura >= 1.20) and (altura <= 1.70) and (peso >= 60) and (peso <= 90):
    print(f'Categoria E')
elif (altura >= 1.20) and (altura <= 1.70) and (peso > 90):
    print(f'Categoria H')
elif (altura > 1.70) and (peso <= 60):
    print(f'Categoria C')
elif (altura > 1.70) and (peso >= 60) and (peso <= 90):
    print(f'Categoria F')
elif (altura>1.70) and (peso > 90):
    print(f'Categoria I')
else:
    print(f'Inválido.')
    
print(f'Exercício 31')
tabela = print(f'Cachorro Quente(100) R$ 1.20, Bauru(101) R$1.30, Bauru com Ovo(102) R$ 1.50')
tabelaA = print(f'Hamburguer(103) R$1.20, Cheeseburguer(104) R$1.70, Suco(105) R$ 2.20, Refri(106) R$ 1.00')

while True:
    print(tabela)
    total = 0
    cod = int(input('Informe o codigo: '))
    qtd = int(input("Digite a quantidade: "))
    if cod == 100:
        total = 1.20 * qtd
    elif cod == 100:
        total = 1.30 * qtd
    elif cod == 102:
        total = 1.50 * qtd
    elif cod == 103:
        total = 1.20 * qtd
    elif cod == 104:
        total = 1.70 * qtd
    elif cod == 105:
        total = 2.20 * qtd
    elif cod == 106:
        total = 1 * qtd
    else:
        print(f'Codigo inválido')
    
    print(f'O total será', total, 'reais!')
    sair = input("Deseja sair? (Y/n) R: ")
    if sair == 'Y':
        print(f'Saindo!')
        break
    elif sair == 'n':
        pass
"""""
## {} [] \
    
        
