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
"""""
#[] {}
print(f'Exercício 14')
