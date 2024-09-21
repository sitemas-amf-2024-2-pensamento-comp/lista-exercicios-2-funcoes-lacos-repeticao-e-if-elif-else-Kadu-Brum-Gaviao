import random

sorteio = random.randint(1, 100)
numEscolhido = int(input('Escolha um número: '))

while True:
    if (numEscolhido < 1) or (numEscolhido > 100):
        print('Número Invalido!')
    elif numEscolhido > sorteio:
        print('O número escolhido é maior que o sorteado.')
    elif numEscolhido < sorteio:
        print('O número escolhido é menor que o sorteado.')
    else:
        break

    numEscolhido = int(input('Escolha outro número: '))
print(f'Parabéns! Você acertou o número: {sorteio}.')
