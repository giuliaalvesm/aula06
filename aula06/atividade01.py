# Calcular média

for i in range(10):
    print(f'Aluno {i+1}')
    nota01 = float(input('Nota 1: '))
    nota02 = float(input('Nota 2: '))
    nota03 = float(input('Nota 3: '))
    nota04 = float(input('Nota 4: '))
    media = (nota01 + nota02 + nota03 + nota04) / 4
    print(f'Média Final: {media}\n')