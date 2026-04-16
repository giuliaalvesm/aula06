resposta = 'S'
while resposta != 'N':
    valor = float(input('Informe o valor da venda: '))
    
    if valor > 1000:
        desconto = valor * 0.1
        valor = -= desconto
        print(f'O valor a pagar é: {valor}')

    resposta = input('Quer continuar [S/N]? ').upper()
print('Programa encerrado')