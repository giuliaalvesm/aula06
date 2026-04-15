# Estrutura de Repetição While
# Números até 10

i = 1
while i <= 10:
    print(i)
    i += 1 #Mesma coisa que i = i+1

#Exemplo
n = 1
soma = 0
while n != 0:
    n = int(input('Digite um número: '))
    soma += n
print(f'Total: {soma}')


#Exemplo
resposta = 'S'
soma = 0
while resposta != 'N':
    n = int(input('Informe um número: '))
    soma += n
    resposta = input('Quer continuar? [S/N] ').upper().strip()[0]
print(f'Total: {soma}')

