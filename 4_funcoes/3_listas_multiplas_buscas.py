# Listas múltiplas: inserção e buscas
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'

while resposta == 'S':
    equipamentos.append(input('Equipamento: ').upper())
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Serial: ')))
    departamentos.append(input('Departamento: ').upper())
    resposta = input('Digite \"S\" para continuar: ').upper()
    print('')

busca = input('\nDigite o nome do equipamento que deseja buscar: ').upper()
for indice in range(0 , len(equipamentos)):
    if busca == equipamentos[indice]:
        print('Valor.......: ', valores[indice])
        print('Serial......: ', seriais[indice])