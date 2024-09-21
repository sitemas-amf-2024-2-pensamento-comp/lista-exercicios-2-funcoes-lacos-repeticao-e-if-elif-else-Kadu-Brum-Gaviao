num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = 0

for i in range(num1, num2 + 1):
    if i % 3 == 0:
        soma += i
        print(f'Número divisivel por 3: {i}')

print(f'A soma dos números divisiveis por 3 é {soma}.')
