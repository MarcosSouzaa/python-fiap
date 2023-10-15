# Usando elif
nome = input('Digite o nome: ')
idade = int(input('Digite a idade: ')) 
doenca_infectocontagiosa = input('Suspeita de doença infectocontagiosa? ').upper()# Converte a string para maiúscula

if idade >= 65:
    print('O paciente ' + nome + ' possui atendimento prioritário!')

elif doenca_infectocontagiosa == 'SIM':
    print('O paciente ' + nome + ' deve ser direcionado para sala de espera reservada!')

else:
    print('O paciente ' + nome + ' não tem atendimento prioritário e pode aguardar na sala comum!')

    '''
      PROBLEMA PARA RESOLVER
      Se o paciente tiver idade >= 65 e doença contagiosa ele está 
      recebendo atendimento prioritário, mas não está indo para sala reservada.

    '''