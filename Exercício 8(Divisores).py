n1 = int(input('Digite um número: '))
i = 1

while i <= n1:
    if n1 % i == 0:
        divisao = n1 // i
        print(f'Dividendo: {n1} / Divisor: {i} = {divisao}')
    i += 1
