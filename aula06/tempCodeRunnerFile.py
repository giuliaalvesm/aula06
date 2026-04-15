resposta = 'S'
soma = 0
while resposta != 'N':
    n = int(input('Informe um número: '))
    soma += n
    resposta = input('Quer continuar? [S/N] ').upper().strip()[0]
print(f'Total: {soma}')