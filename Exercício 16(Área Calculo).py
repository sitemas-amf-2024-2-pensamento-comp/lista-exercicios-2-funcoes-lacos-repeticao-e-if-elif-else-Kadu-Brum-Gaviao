def calcular_area_retangulo(largura, altura):
    area = largura * altura
    return area


largura = float(input('Digite a largura do retangulo: '))
altura = float(input('Digite a altura do retangulo: '))
areaRetangulo = calcular_area_retangulo(largura, altura)

print(f'A área do retangulo é: {areaRetangulo}')
