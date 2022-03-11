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
anguloemrad = float(input("Insira o angulo em radianos: "))
graus = (anguloemrad * 180/3.14)
print("Seu angulo convertido será de:", graus, "graus.")


