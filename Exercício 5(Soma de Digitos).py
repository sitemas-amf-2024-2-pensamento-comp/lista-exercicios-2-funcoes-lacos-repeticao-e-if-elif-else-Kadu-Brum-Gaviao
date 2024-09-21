num = input('Digite um número com mais de um digito: ')
somaDigitos = sum(int(digito) for digito in num)

print(somaDigitos)

if num <= '9':
    print('Digite um número com pelo menos 2 digitos')
