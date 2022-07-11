"""""
print(f'Exercício 1')
print(f'Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar os seguntes passos:')
print(f'A: Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7')
vetor_a = [1, 0 , 5, -2, -5, 7]
print(list(vetor_a))
print(f'B: Armazene em uma variável a soma entre os valores das posições A[0], A[1] e A[5] do vetor e printe na tela a soma.')
soma_especifica = vetor_a[0] + vetor_a[1] + vetor_a[5]
print(f'A soma de {vetor_a[0]} e {vetor_a[1]} e {vetor_a[5]} será {soma_especifica}')
#print(dir(list))
print(f'C: Modifique o vetor {vetor_a[4]}, atribuindo a esta posição o valor 100')
vetor_a.pop(4)
vetor_a.insert(4, 100)
print(f'Após a inserção do valor 100 na posição 4, o vetor ficará assim: {vetor_a}')
print(f'D: Mostre na tela cada valor do vetor A, um em cada linha!')
for element in vetor_a:
    print(element)

print(f'Exercício 2')
qtd_valores = int(input("Insira quantos números deseja adicionar ao vetor: "))
vetor = []
for perguntas in range(qtd_valores):
    valor = int(input("Insira um valor que deseja inserir no vetor: "))
    vetor.append(valor)
print(f'Os valores do vetor A será: {vetor}')

import math
print(f'Exercício 3')
qtd_valores = int(input("Insira quantos números deseja adicionar ao vetor: "))
vetor = []
vetor_quadrado = []
for valores in range(qtd_valores):
    valor = int(input("Insira um valor que deseja inserir no vetor: "))
    vetor.append(valor)
    for valor in vetor:
        quadrado = math.pow(valor, 2)
    vetor_quadrado.append(quadrado)
print(f'Esse será o vetor {vetor}')
print(f'Esse será o vetor ao quadrado {vetor_quadrado}')

print(f'Exercício 4')
qtd_valores = 8
vetor = []
for quantidade in range(qtd_valores):
    valor = int(input('Insira um valor que deseja inserir no vetor: '))
    vetor.append(valor)
print(f'Os valores alocados no vetor serão: {vetor}')
valor_x = int(input("Insira uma posição X dentro do vetor (1-8): "))
valor_y = int(input("Insira uma posição Y dentro do vetor (1-8): "))
valor_x_vetor = vetor[valor_x]
valor_y_vetor = vetor[valor_y]
print(f'A soma dos valores do vetor na posição {valor_x} e {valor_y} será {valor_x_vetor + valor_y_vetor}!')

print(f'Exercício 5')
qtd_valores = 10
vetor = []
lista_pares = []
contador = 0
for valores in range(qtd_valores):
    valor = int(input("Insira um valor: "))
    vetor.append(valor)
print(f'Esses são os valores alocados no vetor {vetor}')
for valor in vetor:
    if valor % 2 == 0:
        lista_pares.append(valor)
        contador += 1
print(f'Nesse vetor temos {contador} numeros pares que são {lista_pares}!')

print(f'Exercício 6')
qtd_valores = 10
vetor = []
for valores in range(qtd_valores):
    valor = int(input("Insira um valor: "))
    vetor.append(valor)
print(f'O maior valor do vetor será {max(vetor)} e o menor valor será {min(vetor)}')

print(f'Exercício 7')
qtd_valores = 10
vetor = []
for valores in range(qtd_valores):
    valor = int(input("Insira um valor: "))
    vetor.append(valor)
print(f'O maior valor alocado no vetor é {max(vetor)} e se encontra na posição {vetor.index(max(vetor))}')

print(f'Exercício 8')
qtd_valores = 6
vetor = []
for valores in range(qtd_valores):
    valor = int(input("Insira um valor: "))
    vetor.append(valor)
print(f'Essa será os valores do vetor em ordem inversa: {vetor[::-1]}')

print(f'Exercício 9')
qtd_valores = 6
vetor = []
for valores in range(qtd_valores):
    valor = int(input("Insira um valor par: "))
    if valor % 2 == 0:
        vetor.append(valor)
    else:
        print(f'O valor só será aceito se for um número par!')
        quit
print(f'Essa será seu vetor de números pares lidos de forma inversa: {vetor[::-1]}')

print(f'Exercício 10')
qtd_alunos = 15
vetor = []
for aluno in range(qtd_alunos):
    nota = float(input("Insira o valor da nota do aluno: "))
    if nota >= 0 and nota <= 10:
        vetor.append(nota)
    else:
        print(f'A nota deverá ser maior ou igual a 0!')
        quit
soma_notas = sum(vetor)
media = soma_notas / qtd_alunos
print(f'A média geral da classe contendo {qtd_alunos} alunos será de {media}!')
"""""
print(f'Exercício 11')
