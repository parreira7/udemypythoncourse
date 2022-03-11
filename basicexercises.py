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

