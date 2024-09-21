"""
Aprovação de Empréstimo:

Crie um programa que simule a aprovação de um empréstimo.
O usuário deve informar o valor do empréstimo, a taxa de juros mensal
e o número de meses para pagar. O programa deve calcular o valor da prestação mensal
e verificar se o valor é maior que 30% do salário do usuário.

"""
# Entradas: 4
# Usuario informa o valor do empréstimo, o número de meses, taxa de juros mensal e salario
valorEmprestimo = float(input('Digite o valor do empréstimo: R$ '))
taxaJuros = float(input('Digite a taxa de juros (em %): '))
numeroMeses = int(input('Digite o número de meses: '))

salarioUsuario = float(input('Digite o salário do usuario: '))

# Processando

# Valor da prestação, conforme
prestacaoMensal = valorEmprestimo * (taxaJuros * (1 + taxaJuros) ** numeroMeses / ((1 + taxaJuros) ** numeroMeses - 1))

limitePrestacao = salarioUsuario * 0.30

if prestacaoMensal > limitePrestacao:
    print(f'Empréstimo não aprovado. A prestação de R$ {prestacaoMensal:.2f} consome mais do que 30% do seu salario')
else:
    print(f'Empréstimo aprovado! A prestação será de R$ {prestacaoMensal:.2f}')
