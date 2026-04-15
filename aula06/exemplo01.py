# Calcula média - 1 aluno
# n1 = float(input('Nota 1: '))
# n2 = float(input('Nota 2: '))
# média = (n1 + n2) / 2
# print('media')

#ESTRUTURA DE REPETIÇÃO (For)
# for num in range(5):
#     print('Olá, mundo!')



qtd = int(input('Quer contar até quanto?'))
for i in range(qtd):
    print(i, end=' ') #Imprime na mesma linha


#soma = 0
for u in range(3):
    print(f'\nRodada {u+1}')
    num1 = int(input('Informe o número: '))
    num2 = int(input('Informe o segundo número: '))
    soma = num1 + num2
    print(f'O total é {soma}')


#VARIÁVEL ACUMULADORA
soma = 0
for i in range(5):
    numero = float(input('Digite o número: '))
    soma = soma + numero

print(f'O total é {soma}')


soma = 0
for v in range(5):
    venda = float(input('\nInforme o valor: '))
    
    if venda >100:
        soma = soma + venda
        print(f'Valor R${venda} somado')
    else:
        print('Valor não computado')

print(f'\nTotal de R$ {soma}')
