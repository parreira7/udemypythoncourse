"""""
print(f'Exercício 1')
for num in range(0, 16, 3):
    print(num, end=' ')
    
print(f'Exercício 2 parte 1')
for num in range(0, 101, 1):
    print(num, end=(' '))

print(f'Exercício 2 parte 2')
num = 0
while (num < 100):
    num = num + 1
    print(num, end=' ')

print(f'Exercício 2 parte 3')
continuar = True
num = 0 
while True:
    if num < 100:
        num = num + 1
        print(num, end=' ')
    else:
        break

print(f'Exercício 3')
num = 11
while (num != 0):
    num = num - 1
    print(num, end=' ')
    
print(f'Exercício 4')
num = -1000
while (num != 100000):
    num = num + 1000
    print(num, end=' ')

print(f'Exercício 5')
num1, num2 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num3, num4 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num5, num6 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num7, num8 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num9, num10 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
numeros = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
soma = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4] + numeros[5] + numeros[6] + numeros[7] + numeros[8] + numeros[9] 
print(f'A soma dos números será {soma}')

print(f'Exercício 6')
num1, num2 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num3, num4 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num5, num6 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num7, num8 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num9, num10 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
soma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
media = soma / 10
print(f'A média será: %.2f' % media)

print(f'Exercício 7')
num1, num2 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num3, num4 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num5, num6 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num7, num8 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num9, num10 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
if num1 < 0  or num2 < 0 or num3 < 0 or num4 < 0 or num5 < 0 or num6 < 0 or num7 < 0 or num8 < 0 or num9 < 0 or num10 < 0:
    print(f'Inválido, pois um número é menor que 0.')
    quit
else:
    soma = soma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
    media = soma / 10
    print(f'A média será: {media}')
    
print(f'Exercício 8')
num1, num2 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num3, num4 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num5, num6 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num7, num8 = int(input("Insira um Número: ")), int(input("Insira um Número: "))
num9, num10 = int(input("Insira um Número: ")), int(input("Insira um Número: "))

numeros = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
print('O maior número será:', max(numeros))

print(f'Exercício 9')
n = int(input("Insira um número: "))
print(n)
i = 0
ímpar = 1
while i < n:
    print(2*i + 1)
    i = i + 1
    
print(f'Exercício 10')
contador = 0
soma = 0
while contador < 50:
    contador += 1
    soma += contador*2
    print(soma, end=' ')

print(f'Exercício 11')
n = int(input("Insira um número: "))
for n in range(0, n + 1, 1):
    print(n, end=' ')
    
print(f'Exercício 12')
n = int(input("Insira um número: "))
for n in range(n, -1, -1):
    print(n, end=' ')
    
print(f'Exercício 13')
n = int(input("Insira um número: "))
for n in range(0, n + 2, 2):
    print(n, end=' ')
    
print(f'Exercício 14')
n = int(input("Insira um numero: "))
for n in range(n, -1, -1):
    print(n, end=' ')
    
print(f'Exercício 15')
n = int(input("Insira um número ímpar positivo: "))
if n % 2 == 0:
    print("Inválido")
    quit
else:
    for n in range(1, n + 2, 2):
        print(n, end=' ')
        
print(f'Exercício 16')
n = int(input("Insira um número positivo ímpar: "))
if n % 2 == 0:
    print('Inválido')
    quit
else:
    for n in range(n, 0, -2):
        print(n, end=' ')
        
print(f'Exercício 17')
n = int(input("Insira um número inteiro positivo: "))
if n > 0:
    print(n)
    for n in range(n, n + n):
        print(n + 1, end=' ')
else:
    quit
    
print(f'Exercício 18')
n, n2 = int(input("Insira um numero: ")), int(input("Insira mais um número: "))
n3, n4 = int(input("Insira mais um número: ")), int(input("Insira mais um número: "))
numeros = [n, n2, n3, n4]
if n > 0 or n2 > 0 or n3 > 0 or n4 > 0:
        print('O maior número será:', max(numeros))
else:
    quit
    
print(f'Exercício 19')
n = int(input("Insira um número: "))
if n > 100 and n <= 999:
    b = str(n)
    for i, v in enumerate(b):
        print(v, end=' ')
else:
    print(f'Inválido')
    quit

print(f'Exercício 20')
p = 0
n = int(input("Digite o número: "))
while n != 1000:
    for n in range(n, 1000 + 2):
        if n % 2 == 0:
            print(f'{n} é par!')
            p = p + 1
        if n >= 1000:
            break
print(f'foram digitados {n} números e {p} deles eram pares!')

        
print(f'Exercício 21')
n, n2 = int(input("Insira um número: ")), int(input("Insira um número: "))
par = 0
impar = 1
for num in range(n, n2, +1):
    if num % 2 == 0:
        par += num
else:
    impar *= num
print(f'par: {par}, impar: {impar}')    

print(f'Exercício 22')
contador = 0 
n = float(input("Quantas notas deseja acrescentar? R: "))
lista = []
for i in range(0, n):
    n = float(input("Insira uma nota de 10 a 20: "))
    lista.append(n)
print(f'{lista}, essas sao as notas!')
soma = sum(lista)
media = soma / n
print(f'A média final será: %.2f' % media)

print(f'Exercício 23')
n = int(input("Insira um número: "))
if n < 0:
    print(f'Inválido, o número tem de ser positivo!')
    quit
else:
    for i in range(1, 1001):
        if n % i == 0:
            print(f'{n} é divisível por {i}')
            
print(f'Exercício 24')
n = int(input("Insira um número positivo: "))
if n < 0:
    print(f'Inválido.')
    quit
else:
    for i in range(1, 1000001):
        if n % i == 0:
            print(f'{n} é divisível por {i}')
def soma_divisores(i):
    divisores = [1]
    for i in range(2, i):
        if n % i == 0:
            divisores.append(i)
    return sum(divisores)
print(f'A soma dos divisores sem contar ele mesmo será:', soma_divisores(n))

print(f'Exercício 25')
for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        print(num, end=' ')
def soma_numeros(num):
    numeros = [1]
    for i in range(1, num):
        if num % num == 0:
            numeros.append(num)
    return sum(numeros)
print(f'\n')
print(f'A soma dos números múltiplos de 3 e 5 será:', soma_numeros(num))

print(f'Exercício 26')
n = int(input("insira um número: "))
for num in range(n, 999):
    if num % 11 == 0 or num % 13 == 0 or num % 17 == 0:
        print(num, end=' ')
        
print(f'Exercício 27')
n = int(input("Insira um numero que deseja harmonizar: "))
um = 1
sequencia = [1/2 for num in range(2, n)]
def harmonica (um, sequencia):
    formula = um + (sequencia)
    return formula
print(f'O número pós harmonizaçao será: %.2f' % harmonica(um, sequencia))

print(f'Exercício 28')
n = int(input("Insira um número: "))
fatorial = 1
for num in range(1, n+1):
    fatorial = fatorial * n
    def formulaE(um, fatorial):
        formula = 1 + (1/fatorial)
        return formula
print(f'O valor de E será: %.2f' % formulaE(fatorial, n))

import math
print(f'Exercício 29')
formulaS = 0 + (1/math.factorial(2) + 2/math.factorial(4)) + (3/math.factorial(6) + 4/math.factorial(8))
print(f'O valor de S será: %.2f' % formulaS)

print(f'Exercício 30 parte 1')
n = int(input("Insira um número: "))
contador = 0
for num in range(0 + 1, n + 1):
    contador = contador + num
    soma = contador + n
print(f'A soma dos números sequenciais, começando de 1 até N, será: %.2f' % soma)


print(f'Exercício 30 parte 2')
n = int(input("Insira um número: "))
lista = []
for num in range(6, n + 1):
    lista.append(num)
    soma = sum(lista)
    formula = 1 - 2 + 3 - 4 + 5 + (soma + (2 * n - 1))
print(formula)
print(lista)

print(f'Exercício 30 Parte 3')
n = int(input("Insira um número: "))
lista = []
if n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 9 == 0:
    for num in range(1, n + 1):
        lista.append(num)
        soma = sum(lista)
        formula = soma + (2 * n - 1)
    else:
        quit
print(formula)
print(lista)

print(f'Exercício 31')
print(f'Faça um programa que calcule e escreva o valor de S:\n S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50\n')
numerador = denominador = 1
resultado = 0
for i in range(50):
   resultado += numerador / denominador
   numerador += 2
   denominador += 1
print(resultado)

print(f'Exercício 32')
print(f'Lançamento de d1 e d2, saída = número de cada dado e a relaçao entre eles (>, <, =) de cada lançamento!')
n = int(input("Insira quantas vezes quer que os dados d1 e d2 sejam lançados: "))
for pergunta in range(n):
    pergunta = d1, d2 = float(input("Insira o valor de d1: ")), float(input("Insira o valor de d2: "))
    while d1 > d2:
        print(f'O dado D1 é maior, visto que, {d1} > {d2}')
        break
    while d2 > d1:
        print(f'O dado D2 é maior, visto que, {d2} > {d1}')
        break
    while d1 == d2:
        print(f'{d1} é igual a {d2}')
        break

print(f'Exercício 33')
n = int(input("Insira quantas vezes deseja adicionar números: "))
for pergunta in range(n):
    n, i, j = int(input("Insira o valor de n: ")), int(input("Insira o valor de i: ")), int(input("Insira o valor de j: "))
    while n % i == 0:
        print(f'{n} é múltiplo de {i}!')
        break
    while n % j == 0:
        print(f'{n} é múltiplo de {j}!')
        break

print(f'Exercício 34')
from math import gcd
def mmc(numeros):
    m = 1
    for n in numeros:
        m = m * n // gcd(m, n)
        return m
numeros = range(2, 21)
print(mmc(numeros))

print(f'Exercício 35')
lista = []
num1, num2 = int(input("Insira o início: ")), int(input("Insira o final: "))
for numero in range(num1, num2 + 1, 2):
    addlista = lista.append(numero)
    soma = sum(lista)
print(lista)
print(f'A soma dos números impares no intervalo de {num1} até {num2} será {soma}!')

import math
print(f'Exercício 36')
contador = 0
for i in range(1, 10 + 1):
    i += i
    potenciaçao = math.pow(i, 2)
print(potenciaçao)
lista = []
for i in range(1, 10 + 1):
    addlista = lista.append(i)
soma = sum(lista)
potencia = math.pow(soma, 2)
print(potencia)
diferenca = potencia - potenciaçao
print(f'A diferença entre a soma dos quadrados dos dez primeiros numeros naturais e o quadrado da soma é {potencia} - {potenciaçao} = {diferenca}')

print(f'Exercício 37')
lista = []
for i in range(1000, 10000):
    lista.append(i)
for i in lista:
    k = str(i)
    k = list(k)
    numero1 = k[0] + k[1]
    numero2 = k[2] + k[3]
    if (int(numero1) + int(numero2)) ** 2 == i:
        print(i)

import math
print(f'Exercício 38')
a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
def pitagoras(a, b):
    formula = math.pow(a, 2) + math.pow(b, 2)
    return formula
result = pitagoras(a, b)
print(f'{a}² + {b}² = {a ** 2} + {b ** 2} = {result} = {math.sqrt(result)}²')

print(f'Exercício 39')
base = float(input("Insira um valor para a base do triangulo: "))
altura = float(input("Insira um valor para a altura do triangulo: "))
if base >= 1 and altura >= 1:
    calculo = base * altura 
    divisao = calculo / 2 
    print(f'Tendo a base no valor de {base} e altura {altura}, usando a fórmula Area = Base * Altura / 2')
    print(f'A área do triangulo será {divisao}')
else:
    print(f'Inválido')
    quit

print(f'Exercício 40')
lista = []
while True:
    n = int(input("Insira um número inteiro: "))
    lista.append(n)
    if n <= 0:
        lista.pop()
        print(f'O número deve ser um número inteiro!')
        break
print(f'Números na lista: {lista}')
print(f'O maior número é {max(lista)} e o menor número é {min(lista)}.')

from fractions import Fraction
print(f'Exercício 41')
def conta(r1, r2):
    r = (r1 * r2)
    fraçao = (Fraction(r1 + r2))
    result = r / fraçao
    return result
while True:
    r1, r2 = int(input("Insira o valor de R1: ")), int(input("Insira o valor de R2: "))
    if r1 >= 1 and r2 >= 1:
        print(f'O resultado da associação em paralelo de dois resistores será: {conta(r1, r2)}!')
    else:
        print(f'{r1} ou {r2} devem ser maiores que zero!')
        break

import math
print(f'Exercício 42')
while True:
    n = int(input("Insira um número: "))
    if n >= 1:
        print(f'O quadrado desse número é: {math.pow(n, 2)}, o cubo é: {math.pow(n, 3)} e a raiz quadrada será {math.sqrt(n)}!')
    else:
        print(f'O {n} deve ser um inteiro!')
        break

print(f'Exercício 43')
lista = []
while True:
    idade = int(input("Insira uma idade: "))
    if idade >= 1:
        lista.append(idade)
    else:
        print(f'Essas são as idades: {lista}')
        lista.pop()
        tamanho = len(lista)
        print(f'Temos {tamanho} idades nesta lista!')
        print(f'A média das idades será: {(sum(lista)) / tamanho}')
        break

print(f'Exercício 44')
num = int(input("Quantos numeros da sequencia de Fibonacci deseja inserir? R: "))
x1 = 0
x2 = 1
fibo_n = 0
while(x2 <= num):
    fibo_n = x1 + x2
    print(f'{fibo_n}', end=' ')
    x1 = x2
    x2 = fibo_n

print(f'Exercício 45')
while True:
    velocidade_kmporh = float(input("Insira uma velocidade km/h: "))
    velocidade_mpors = float(input("Insira uma velocidade m/s: "))
    pergunta = input("Deseja converter de km/h para m/s (1) ou m/s para km/h? (2) (3 PARA SAIR): ")
    if pergunta == '1':
        print(f'A velocidade convertida de km/h para m/s será {velocidade_kmporh / 3.6}')
    elif pergunta == '2':
        print(f'A velocidade convertida de m/s para km/h será {velocidade_mpors * 3.6}')
    else:
        print(f'Finalizando o sistema...')
        break

import random
print(f'Exercício 46')
tentativas = 0
while True:
    numero = random.randint(1, 1000)
    pergunta = int(input("Insira um chute de 1 a 1000: "))
    if pergunta != numero:
        tentativas += 1
        print(f'{pergunta} não é o número certo, tente novamente!')
    else:
        print(f'Você acertou o número {numero} com {tentativas} tentativas!')
        break

print(f'Exercício 47')
operaçoes = ('Operações: adição(1), subtração (2), multiplicação (3), divisão (4), sair (5)')
while True:
    print(f'{operaçoes}')
    pergunta = int(input("Insira alguma das operações do menu: "))
    num1, num2 = int(input("Insira um número: ")), int(input("Insira um número: "))
    if pergunta == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif pergunta == 2:
        print(f'{num1} - {num2} = {num1 - num2}')
    elif pergunta == 3:
        print(f'{num1} * {num2} = {num1 * num2}')
    elif pergunta == 4:
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print(f'Finalizando o sistema...')
        break

print(f'Exercício 48')
lista = []
listapar = []
x1 = 0
x2 = 1
fibo_n = 0
while(x2 <= 400000000):
    fibo_n = x1 + x2
    print(f'{fibo_n}', end=' ')
    x1 = x2
    x2 = fibo_n
    lista.append(x2)
for element in (lista):
    if element % 2 == 0:
        listapar.append(element)
print(f'\n')
print(f'{listapar} são os números pares da sequência!')
print(f'\n{sum(listapar)} é o resultado da soma dos números pares da sequência!')

print(f'Exercício 49')
funcionarios = ['Carlos', 'João']
meses = 0
while True:
    salario, qtd_meses = int(input("Insira o salário que Carlos irá receber: ")), int(input(f"Quantos meses {funcionarios[0]} irá investir? R: "))
    if salario >= 1:
        salariojoao  = salario / 3
        print(f'{funcionarios[1]}, recebe R${salariojoao} enquanto {funcionarios[0]} recebe R${salario}!')
        for num in range(0, qtd_meses):
            salario += (salario * 0.5)
        while salario > salariojoao:
            meses += 1
            salariojoao += (salariojoao * 0.2)
        print(f'{funcionarios[1]} precisa investir por {meses} meses para receber R${salariojoao} e ficar equivalente ou ultrapassar a quantia de R${salario} de {funcionarios[0]}')
    else:
        print(f'Finalizando o sistema...')
        break

print(f'Exercício 50')
altura_chico = 1.5
altura_ze = 1.1
anos = int(input("Insira quantos anos deseja estimar: "))
for ano in range(0, anos, 1):
    altura_chico += 0.02
    altura_ze += 0.03
while altura_ze <= altura_chico:
    anos += 1
    print(f'Zé precisará de {anos} anos para ultrapassar a altura de {altura_chico}.')
    break

print(f'Exercício 51')
ano_atual = 2022
salario_1997 = 2294
ano = 1997
aumento = 0.15
for n in range(ano, ano_atual + 1, 1):
    aumento = aumento + (aumento * 2)
    salario_1997 += aumento
    print(f'O salário em {n} será de R${int(salario_1997)}!')

print(f'Exercício 52')
notas = [100, 50, 20, 10, 5, 2, 1]
while True:
    saque = float(input("Insira o valor que será sacado: "))
    if saque >= 1:
        cem, saque = int(saque / notas[0]),  saque % 100
        cinquenta, saque = int(saque / notas[1]),  saque % 50
        vinte, saque = int(saque / notas[2]),  saque % 20
        dez, saque = int(saque / notas[3]),  saque % 10
        cinco, saque = int(saque / notas[4]),  saque % 5
        dois, saque = int(saque / notas[5]),  saque % 2
        um, saque = int(saque / notas[6]),  saque % 1
        um = saque
        print(f'Notas de R$100 necessárias: {cem}')
        print(f'Notas de R$50 necessárias: {cinquenta}')
        print(f'Notas de R$20 necessárias: {vinte}')
        print(f'Notas de R$10 necessárias: {dez}')
        print(f'Notas de R$5 necessárias: {cinco}')
        print(f'Notas de R$2 necessárias: {dois}')
        print(f'Notas de R$1 necessárias: {um}')
    else:
        print(f'Finalizando o sistema...')
        break


print(f'Exercício 53')
num = 1
num_final = int(input("Insira a quantidade de linhas desejadas: "))
for n in range(1, num_final + 1):
    for i in range(1, n + 1):
        print(num, end= ' ')
        num += 1
    print()

print(f'Exercício 54')
while True:
    n = int(input("Insira um numero inteiro: "))
    if n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 9 == 0:
        print(f'{n} é primo!')
    else:
        print(f'{n} não é primo, finalizando o sistema...')
        break

print(f'Exercício 55')
lista = []
while True:
    n = int(input("Insira um numero inteiro: "))
    if n >= 1:
        for numero in range(0 , n + 1):
            if numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0 or numero % 9 == 0:
                lista.append(numero)
    print(f'A soma dos números primos na lista: {lista} será {sum(lista)}!')

print(f'Exercício 56')
lista = []
for numero in range(0, 19999999):
    if numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0 or numero % 9 == 0:
        lista.append(numero)
print(f'A soma dos números primos na lista será {sum(lista)}!')

print(f'Exercício 57')
a, b = int(input("Insira o valor de A: ")), int(input("Insira o valor de B: "))
lista = []
contador = 0
for numeros in range(a, b + 1):
    if numeros % 3 == 0 or numeros % 5 == 0 or numeros % 7 == 0 or numeros % 9 == 0:
        lista.append(numeros)
        contador += 1
print(f'Existem {contador} números primos no intervalo de {a} até {b}!')

print(f'Exercício 58')
a, b = int(input("Insira o valor de A: ")), int(input("Insira o valor de B: "))
lista = []
contador = 0
for numeros in range(a, b + 1):
    if numeros % 3 == 0 or numeros % 5 == 0 or numeros % 7 == 0 or numeros % 9 == 0:
        lista.append(numeros)
        contador += 1
print(f'Existem {contador} números primos no intervalo de {a} até {b}!')
print(f'E a soma de tais números será de {sum(lista)}.')

print(f'Exercício 59')
lista = []
def formula(potencia, horas, dias_no_mes):
    consumo = (potencia * horas) * (dias_no_mes / 1000)
    return consumo
while True:
    habitantes = int(input("Insira o total de habitantes na cidade: "))
    if habitantes >= 1:
        valor = float(input("Insira o valor de KWH: "))
        potencia = int(input("Insira o valor da potência (W): "))
        horas = int(input("Insira a quantidade de horas de uso por dia: "))
        dias_no_mes = int(input("Insira o valor de dias de uso no mês: "))
        resultado = ((habitantes * valor) / habitantes) * formula(potencia, horas, dias_no_mes)
        print(f'O resultado do consumo por habitante será R${int(resultado)}.')
    else:
        print(f'Finalizando o sistema...')
        break

print(f'Exercício 60')
lista = []
contador = 0
while True:
    print(f'Menu: \n (A) = Soma dos números digitados \n (B) = A quantidade de números digitados \n (C) = A média dos números digitados \n (D) = O maior número digitado \n (E) = O menor número digitado \n (F) = A média dos números pares')
    pergunta = input("Insira alguma opção do menu de (A) até (F), digite (0) para finalizar o sistema: ")
    while pergunta == 'A' or pergunta == 'a':
        perguntas = int(input("Insira quantos números deseja inserir: "))
        for pergunta in range(perguntas):
            numero = int(input("Insira um número inteiro: "))
            lista.append(numero)
        print(f'A soma dos números digitados será {sum(lista)}')
    while pergunta == 'B' or pergunta == 'b':
        perguntas = int(input("Insira quantos números deseja inserir: "))
        for pergunta in range(perguntas):
            numero = int(input("Insira um número inteiro: "))
            contador += 1
        print(f'Foram inseridos {contador} números.')
    while pergunta == 'C' or pergunta == 'c':
        perguntas = int(input("Insira quantos números deseja inserir: "))
        for pergunta in range(perguntas):
            numero = int(input("Insira um número inteiro: "))
            lista.append(numero)
        print(f'A soma dos números digitados é {sum(lista)} e a média será {sum(lista) / pergunta} pois fora inserido {perguntas} números.')
    while pergunta == 'D' or pergunta == 'd':
        perguntas = int(input("Insira quantos números deseja inserir: "))
        for pergunta in range(perguntas):
            numero = int(input("Insira um número inteiro: "))
            lista.append(numero)
        print(f'O maior número inserido foi {max(lista)}')
    while pergunta == 'E' or pergunta == 'e':
        perguntas = int(input("Insira quantos números deseja inserir: "))
        for pergunta in range(perguntas):
            numero = int(input("Insira um número inteiro: "))
            lista.append(numero)
        print(f'O menor número digitado foi {min(lista)}')
    while pergunta == 'F' or pergunta == 'f':
        perguntas = int(input("Insira quantos números deseja inserir: "))
        for pergunta in range(perguntas):
            numero = int(input("Insira um número inteiro: "))
            if numero % 2 == 0:
                lista.append(numero)
        print(f'A soma dos números pares será {sum(lista)}.')
    if pergunta == 0:
        print(f'Finalizando sistema...')
        break

print(f'Exercício 61')
from itertools import product
num_palindromes = (i*j for i, j in product(range(100, 1000), repeat=2) if str(i*j) == str(i*j)[::-1])
print(f'O maior palíndromo encontrado foi {max(num_palindromes)}!')
"""""
#[] {} \
