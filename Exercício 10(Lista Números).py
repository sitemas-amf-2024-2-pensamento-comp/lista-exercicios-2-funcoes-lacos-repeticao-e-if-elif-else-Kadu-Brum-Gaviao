n = 0
maiorLista = 0
menorLista = 0

lista = []

for i in range(n, 5):
    n = int(input('Digite um número: '))
    lista.append(n)
    print(lista)
    maiorLista = max(lista)
    menorLista = min(lista)
print(f'O maior número da lista é: {maiorLista}')
print(f'O menor número da lista é: {menorLista}')