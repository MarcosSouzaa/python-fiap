# Depreciação e exclusão
inventario = []
resposta = 'S'

# adicionar item no inventario
while resposta == 'S':
    equipamento = [input('Equipamento: ').upper(), 
                   float(input('Valor: ')),
                   int(input('Número serial: ')),
                   input('Departamento: ').upper()]
     
    inventario.append(equipamento)
    resposta = input('Digite "S" para continuar: ').upper()
    print('')
#exibir dados do inventário
for elemento in inventario:
    print('Nome................:', elemento[0])
    print('Valor...............:', elemento[1])
    print('Serial..............:', elemento[2])
    print('Departamento........:', elemento[3])

#localizar um item no inventario
busca = input('\nDigite o nome do equipamento que deseja buscar: ').upper()
for elemento in inventario:
    if busca == elemento[0]:
        print('Valor......: ', elemento[1])
        print('Serial.....: ', elemento[2])

#depreciar itens no inventario
depreciacao = input('\nDigite o nome do equipamento que será depreciado: ').upper()
for elemento in inventario:
    if depreciacao == elemento[0]:
        print('Valor antigo: ', elemento[1])
        elemento[1] = elemento[1] * 0.9
        print('Novo valor: ', elemento[1])

#excluir um item do inventario       
serial = int(input('\nDigite o serial do equipamento que será excluido: ').upper())
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print('Nome................:', elemento[0])
    print('Valor...............:', elemento[1])
    print('Serial..............:', elemento[2])
    print('Departamento........:', elemento[3])

#resumo de valores do inventário
valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print('O equipamento mais caro custa: ', max(valores))
    print('O equipamento mais barato custa: ', min(valores))
    print('O total de equipamentos é de: ', sum(valores))
