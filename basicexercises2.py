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
n = int(input("Quantas notas deseja acrescentar? R: "))
lista = []
for i in range(0, n):
    n = int(input("Insira uma nota de 10 a 20: "))
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
"""""
#[] {} \

