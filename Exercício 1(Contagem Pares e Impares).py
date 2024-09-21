"""
Contagem de Números Pares e Ímpares:

Escreva um programa que receba um número inteiro positivo n do usuário
e exiba todos os números pares e ímpares de 1 até n.
"""

num = int(input('Digite um número: '))
i = 1

for i in range(num + 1):
    if i % 2 == 0:
        print(f'O número {i} é par!')
    else:
        print(f'O número {i} é impar!')
