"""
print('Exercício 1 e 2')

#Num Inteiro
print('\nNum Inteiro')
numQ = int(input('Digite um numero inteiro: '))
for numQ in range(-numQ, numQ + 1):
    print(numQ, end=' ')
print(f'\nFoi apresentado desde o negativo até o positivo', end='\n')
#Num Real
print('\nNum Real')
numR = float(input('Digite um numero real: '))
print('\nO seu numero real escolhido foi:', numR)

print('Exercício 3')

valor1 = int(input('\nDigite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro e último valor: '))
print("A soma dos tres valores apresentados é:", valor1 + valor2 + valor3)

print("Exercício 4")
numreal = int(input('\nDigite um número qualquer: '))
print('O quadrado do seu número é:', numreal ** 2)

print("Exercício 5")
numI = int(input("\nDigite um número inteiro (positivo ou negativo): "))
print("A quinta parte do seu número representa:", numI / 1/5)

print("Exercício 6")
tempC = float(input('\nInsira a temperatura em Celsius: '))
fahren = (tempC * (9/5) + 32)
print("Sua temperatura em Fahrenheit é:", fahren)

print("Exercício 7")
tempF = float(input('\nInsira a temperatura em Fahrenheit: '))
celsius = (5 * (tempF - 32) / 9)
print("Sua temperatura em Celsius é:", celsius)

print("Exercício 8")
tempK = float(input("\nInsira a temperatura em Kelvin: "))
celsius = (tempK - 273.15)
print("Sua temperatura em Celsius é:", celsius)

print("Exercício 9")
tempC = float(input("\nInsira a temperatura em Celsius: "))
kelvin = (tempC + 273.15)
print("Sua temperatura em Kelvin é:", kelvin)

print("Exercício 10")
velocidade_km = float(input('\nInsira uma velocidade em km/h: '))
conversao_km_to_m = (velocidade_km / 3.6)
print("Sua velocidade em metros por segundo é de aproximadamente:", conversao_km_to_m)

print("Exercício 11")
velocidade_ms = float(input("\nInsira a velocidade de metros por segundo: "))
kmporh = (velocidade_ms * 3.6)
print("Sua velocidade em km por hora é de:", kmporh)

print("Exercício 12")
milhas = float(input("\nInsira a velocidade em milhas: "))
kmporh = (1.61 * milhas)
print("Sua velocidade em km por hora é de:", kmporh)

print("Exercício 13")
km = float(input("\nInsira a distancia em KM: "))
milhas = (km / 1.61)
print("A distancia em milhas será de:", milhas)

print("Exercício 14")
anguloemgraus = float(input("\nInsira o angulo em graus: "))
radianos = (anguloemgraus * 3.14 / 180)
print("Seu angulo em radianos será de:", radianos, "radianos")

print("Exercício 15")
anguloemrad = float(input("\nInsira o angulo em radianos: "))
graus = (anguloemrad * 180/3.14)
print("Seu angulo convertido será de:", graus, "graus.")

print("Exercício 16")
polegadas = float(input("\nInsira o tamanho em polegadas: "))
centimetros = (polegadas * 2.54)
print("O tamanho convertido para centímetros será de: %.2f" % centimetros)

print("Exercício 17")
cm = float(input("\nInsira o comprimento em centímetros: "))
polegadas = (cm / 2.54)
print("O tamanho em polegadas será de: %.2f" % polegadas)

print("Exercício 18")
m3 = float(input("\nInsira o Volume em M³: "))
litro = (m3 * 1000)
print(m3, "metros cúbicos suportará: %.2f" % litro, "litros")

print("Exercício 19")
litros = float(input("\nInsira o volume em litros: "))
m3 = (litros / 1000)
print(litros, "litros vale por %.2f" % m3, "metros cúbicos")

print("Exercício 20")
massa = float(input("\nInsira a massa em quilogramas: "))
print("\nAgora será convertido para libras!\n")
libras = (massa / 0.45)
print(massa, "quilos equivale por: %.2f libras" % libras)

print("Exercício 21")
massaL = float(input("\nInsira a massa em libras: "))
print("\nAgora será convertido para quilos!\n")
quilos = (massaL * 0.45)
print(massaL, "libras equivale por: %.2f quilos" % quilos)

print("Exercício 22")
jardas = float(input("\nInsira o valor do comprimento em jardas: "))
print("\nAgora o valor será convertido para metros!\n")
metros = (jardas * 0.91)
print(jardas, "jardas equivale por: %.2f metros." % metros)

print("Exercício 23")
metros = float(input("\nInsira o valor do comprimento em metros: "))
print("\nAgora o valor será convertido para jardas!\n")
jardas = (metros / 0.91)
print(metros, "metros equivalem por: %.2f jardas!\n" % jardas)

print("Exercício 24")
hectares = float(input("\nInsira o valor do comprimento em hectares: "))
print("\nAgora o valor será convertido para metros quadrados!\n")
m2 = (hectares * 10000)
print(hectares, "hectares equivalem por: %.2f metros quadrados!\n" % m2)

print("Exercício 28")
valor1 = int(input("\nInsira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))
valor3 = int(input("Insira o último valor: "))
soma = (valor1 ** 2) + (valor2 ** 2) + (valor3 ** 2)
print("\nA soma dos quadrados dos 3 valores inseridos é de: %.2f!" % soma)

print("Exercício 29")
nota1 = float(input("\nInsira o valor da primeira nota: "))
nota2 = float(input("Insira o valor da segunda nota: "))
nota3 = float(input("Insira o valor da terceira nota: "))
nota4 = float(input("Insira o valor da última nota: "))
print("\nAgora será feita a média aritmética!\n")
media = (nota1 + nota2 + nota3 + nota4) 
mediaA = media / 4
print("O cálculo da média das notas será de: %.2f\n" % mediaA)

print("Exercício 30")
real = float(input("Insira o valor em real: "))
dolar_hoje = float(input("Insira o valor do dolar hoje: "))
conversao = (real / dolar_hoje)
print("\nAgora o valor será convertido para dólar!\n")
print(real, "reais equivalem por: %.2f dólares\n" % conversao)

print("Exercício 31")
numero = int(input("\nInsira um valor: "))
if numero is not None:
    print(numero - 1, numero, numero + 1)
    
print("Exercício 32")
valor = int(input("\nInsira um valor: "))
sucessor = (valor * 3 + 1) 
antecessor = (valor * 2 - 1)
soma = (sucessor + antecessor)
print("A soma dos sucessores e antecessores multiplicados será de: %.2f\n" % soma)

print("Exercício 33")
lado = int(input("\nInsira o valor do lado de um quadrado: "))
lado1 = int(input("Insira o valor do segundo lado do quadrado: "))
ladoxlado = (lado * lado1)
print("\nTais valores obtidos dos lados equivalem por: %.2f cm² ou m².\n" % ladoxlado)

print("Exercício 34")
raio = float(input("\nInsira o valor do raio de um círculo: "))
print("\nAgora será exibido a área de tal círculo!\n")
pi = (3.141592)
raioquadrado = (raio ** 2)
calculo = (raioquadrado * pi)
print(raio, "como raio equivalera em uma área de: %.2f\n" % calculo)

print("Exercício 35")
from math import isqrt
a = int(input("\nInsira o valor de A: "))
b = int(input("Insira o valor de B: "))
elev_a = (a ** 2)
elev_b = (b ** 2)
raizquadrada = isqrt(elev_a + elev_b)
print("\nAgora será calculado o valor da hipotenusa!\n")
print("O valor será de:", raizquadrada)

print("Exercício 36")
altura = float(input("\nInsira o valor da altura do cílindro circular: "))
raio = float(input("Insira o valor do raio do cílindro circular: "))
pi = (3.141592)
raioquadrado = (raio ** 2)
formula = (pi * raioquadrado * altura)
print("\nO valor do volume do cilindro será de: %.2f cm³ ou m³" % formula)

print("Exercício 37")
valor = float(input("\nInsira o valor do produto: "))
print("Foi descontado aproximadamente 12 porcento do valor total!\n")
desconto = (valor * 0.12)
resultado = (valor - desconto)
print("\nCom o desconto de 12 porcento o valor ficará por: %.2f" % resultado)

print("Exercício 38")
salario = float(input("\nInsira o seu salário: "))
print("Uau, voce recebeu um aumento de 25%!")
aumento = (salario * 0.25)
salarioF = (salario + aumento)
print("\nCom o aumento de 25 porcento no salário, vc receberá: %.2f" % salarioF)

print("Exercício 39")
premio = (780.000)
print(f"\nO premio será de: ", premio, "mil reais!")
primeiro_ganhador = (premio * 0.46)
primeiro_g = (premio - primeiro_ganhador)
print("O primeiro ganhador receberá: %.2f mil reais!" % primeiro_g)
premio = (780.000)
segundo_ganhador = (premio * 32 /100)
segundo_g = (segundo_ganhador)
print("O segundo ganhador receberá: %.2f mil reais!" % segundo_g)
premio = (780.000)
terceiro_ganhador = (premio * 22 /100)
terceiro_g = (terceiro_ganhador)
print("O terceiro ganhador receberá: %.2f mil reais!" % terceiro_g)
print("\n")

print("Exercício 40")
pgtopordia = (30)
print("O pagamento será de R$%.2f por dia!" % pgtopordia)
print("Entretanto, teremos um desconto de 8 porcento do total.\n")
dias = int(input("Insira os dias trabalhados: "))
diasxpgto = (dias * pgtopordia)
desconto = (diasxpgto * 0.08)
total = (diasxpgto - desconto)
print("O valor a ser pago será de: R$%.2f por dias trabalhados!" % total)
print("\n")

print("Exercício 41")
valorporhoras = float(input("\nInsira o valor por hora trabalhada em R$: "))
horastrabalhadas = float(input("Insira o valor de horas trabalhadas ao mes: "))
aserpago = (valorporhoras * horastrabalhadas)
aumento10 = (aserpago * 0.10)
total = (aserpago + aumento10)
print("O valor recebido por horas trabalhadas será de: R$%.2f" % total)
print("\n")

print("Exercício 42")
salariobase = float(input("\nInsira o seu salário por mes: "))
print("Voce tem uma gratificaçao de 5%!")
gratificaçao = (salariobase * 0.05)
gF = (salariobase + gratificaçao)
print("Após receber a gratificaçao voce receberá: R$%.2f" % gF)
print("\nAgora terá de pagar 7 porcento de imposto de renda :/")
imposto = (gF * 0.07)
iF = (gF - imposto)
print("Após o desconto dos impostos, voce receberá: R$%.2f\n" % iF)

print("Exercício 43")
print("\nPrograma de ajuda aos vendedores!")
aserpago = float(input("Insira o valor a ser pago: R$ "))
aserpago10pct = (aserpago * 0.10)
aserpagoF = (aserpago - aserpago10pct)
print("O valor a ser pago com desconto de 10 porcento será de: R$%.2f" % aserpagoF)
print("\n")
print("O valor parcelado em 3x!")
parcelado = (aserpago / 3)
print("Parcelado em 3x, o valor será de: R$%.2f" % parcelado)
print("\n")
comissao = (aserpagoF * 0.05)
print("A comissao do vendedor perante o produto com desconto será de: R$%.2f" % comissao)
print("\n")
comissaoParcelada = (aserpago * 0.05)
print("A comissao do vendedor caso o comprador parcele, será de: R$%.2f" % comissaoParcelada)

print("Exercício 44")
altura_degrau = float(input("\nDigite a altura do degrau em cm: "))
altura_subir = float(input("Digite quanto desejará subir em cm: "))
altura_por_degrau = (altura_subir / altura_degrau)
print("\nPara conseguir subir %.2f centímetros..." % altura_subir)
print("O usuário deverá subir: %.2f degraus!" % altura_por_degrau)
print("\n")

print("Exercício 45")
print("\nConversor de maiúscula para minúscula em ASCII\n")
letra = input("Insira a letra maiúscula: ")
conversao = ord(letra)
print("\nO valor ASCII da letra é de:", conversao)
letraconvertida = chr(ord(chr(conversao)) + 32)
print("\nR:", letraconvertida)
print("\n")

print("Exercício 46")
#Ler 3 números inteiros
print("\nValor invertido com 3 dígitos!")
numero = int(input("Insira um número inteiro com 3 dígitos: "))
numero = str(numero)
print("Seu número invertido será:", numero[::-1])
print("\n")

print("Exercício 47\n")
print("Leitor de número de 4 digitos!")
primeirovalor = int(input("Insira o primeiro dígito: "))
segundovalor = int(input("Insira o segundo dígito: "))
terceirovalor = int(input("Insira o terceiro dígito: "))
quartovalor = int(input("Insira o último dígito: "))
print("\n", primeirovalor, "\n", segundovalor, "\n", terceirovalor, "\n", quartovalor)
print("\n")

print("Exercício 48\n")
print("Conversor de segundos para horas, minutos e segundos!")
segundos = int(input("Quantos segundos deseja converter: "))
horas = (segundos / 3600 )
minutos = (horas / 60)
segundosfinais = (minutos / 60)
print("De acordo com a conversão, o horário será:", horas, "horas", minutos, "minutos", segundosfinais, "segundos")

print("Exercício 49\n")
print("Leitor de horas, minutos e segundos de uma experiência biológica!\n")
print("O teste iniciou em: ")
iniciohoras = int(input("Insira a hora em que se iniciou: "))
iniciominutos = int(input("Insira os minutos em que se iniciou: "))
iniciosegundos = int(input("Insira os segundos em que se iniciou: "))
horasantigas = int(input("Insira as horas necessárias para o experimento: "))
minutosantigos = int(input("Insira os minutos necessários para o experimento: "))
segundosantigos = int(input("Insira os segundos necessários para o experimento: "))
print("\nApós o termino da experiência, se passaram: ")
print(horasantigas, "horas,", minutosantigos, "minutos,", segundosantigos, "segundos.")
horaatual = (iniciohoras + horasantigas)
minutoatual = (iniciominutos + minutosantigos)
segundoatual = (iniciosegundos + segundosantigos)
print("\nLogo, o horário atual será:", horaatual, "horas,", minutoatual, "minutos,", segundoatual, "segundos!")

print("Exercício 50")
print("Calculadora de ano - idade\n")
ano = (2022)
idade = int(input("Insira a sua idade: "))
ano_idade = (ano - idade)
print("Você nasceu em:", ano_idade)

print("Exercício 51")
print("Leitor de coordenadas x e y no ponto R² de origem!\n")
x1 = int(input(f'x1 => '))

y1 = int(input(f'y1 => '))

calculo = int((((0 - x1) ** 2) + ((0 - y1) ** 2)) ** (1 / 2))

print(f'A distância entre a origem (0,0) e o ponto de'

     f' coordenadas ({x1},{y1}) é: {calculo}')

# Demonstrando o cálculo

print(f'x2 - x1 = {0 - x1}, \n'

     f'y2 - y1 = {0 - y1}')

print(f'(x2 - x1) ** 2 = {(0 - x1) ** 2}, \n'

     f'(y2 - y1) ** 2 = {(0 - y1) ** 2}')

print(f'Distância da origem = {calculo}\n')

print(f'Exercício 52\n')
premio = float(input("Insira o premio total: "))
ganhadorA = float(input("Quanto o primeiro ganhador apostou? R$"))
ganhadorB = float(input("Quanto o segundo ganhador apostou? R$"))
ganhadorC = float(input("Quanto o terceiro ganhador apostou? R$"))
resultado_1 = 0.5 * premio
resultado_2 = 0.35 * premio
resultado_3 = 0.15 * premio
print('\n')
print(f'De acordo com o premio estipulado, o primeiro ganhador ganhou R$%.2f reais' % resultado_1)
print(f'De acordo com o premio estipulado, o segundo ganhador ganhou R$%.2f reais' % resultado_2)
print(f'De acordo com o premio estipulado, o terceiro ganhador ganhou R$%.2f reais' % resultado_3)
print('\n')

print(f'Exercício 53\n')
t_comprimento = float(input("Insira o comprimento do terreno:"))
t_largura = float(input("Insira a largura do terreno:"))
m2 = t_comprimento * t_largura
print(f'Área do terreno:%.2f m²\n' % m2)
preco_tela = float(input("Insira o preço da tela por metro: R$"))
preco_por_m = preco_tela * m2
print(f'O preço para cobrir todo o terreno com tela será de R$%.2f reais\n' % preco_por_m)
"""

