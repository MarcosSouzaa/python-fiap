# O índice é o eindicador da lista.
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'

while resposta == 'S':
   equipamentos.append(input('Digite o equipamento: ').upper())
   valores.append(float(input('Digite o valor: ')))
   seriais.append(input('Digite o serial: '))
   departamentos.append(input('Digite o departamento: ').upper())

   resposta = input('Digite \"S\" para continuar: ').upper()

   for indice in range(0, len(equipamentos)):
      print('\nEquipamento..:', (indice+1))
      print('Nome...........:', equipamentos[indice])
      print('Valor..........:', valores[indice])
      print('Serial.........:', seriais[indice])
      print('Departamento...:', departamentos[indice])
      print('')