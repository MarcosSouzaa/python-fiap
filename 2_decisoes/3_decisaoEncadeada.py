# USANDO DECISÃO ENCADEADA

nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
doenca_infectoContagiosa = input('Suspeita de doença infectocontagiosa? ').upper()

if idade >= 65:
    print('Paciente com prioridade!')
    if doenca_infectoContagiosa == 'SIM':
        print('Encaminhe o paciente para sala AMARELA!')
    elif doenca_infectoContagiosa == 'NÃO':
        print('Encaminhe o paciente para sala BRANCA!')
    else:
        print('Responda a suspeita de doença infectocontagiosa com SIM ou NÃO')
else:
    print('Paciente sem prioridade!')
    if doenca_infectoContagiosa == 'SIM':
        print('Mas devido a suspeita, encaminhe o paciente para sala AMARELA!')
    elif doenca_infectoContagiosa == 'NÃO':
        print('Encaminhe o paciente para sala BRANCA!')
    else:
         print('Responda a suspeita de doença infectocontagiosa com SIM ou NÃO')