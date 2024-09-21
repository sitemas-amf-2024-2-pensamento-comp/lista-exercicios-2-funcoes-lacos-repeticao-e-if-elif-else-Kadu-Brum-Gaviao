"""
Números Primos:

Desenvolva um programa que receba um número inteiro
positivo do usuário e verifique se ele é um número primo.

"""
num = int(input('Digite um número inteiro: '))

if num <= 1:
    print(f'O número {num} não é primo!')
else:
    for i in range(2, num - 1):
        if num % i == 0:
            print(f'O número {num} não é primo!')
            break
    else:
        print(f'O número {num} é primo!')