# Usando elif e o operador AND
nome = input('Digite o nome: ')
idade = int(input('Digite a idade: ')) 
doenca_infectocontagiosa = input('Suspeita de doença infectocontagiosa? ').upper()# Converte a string para maiúscula

if idade >= 65 and doenca_infectocontagiosa == 'SIM':
    print('O (a) paciente ' + nome + ' deve ser direcionado para sala de espera reservada!')

elif idade >= 65 and doenca_infectocontagiosa == 'NÃO':
    print('O (a) paciente ' + nome + ' possui atendimento prioritário!')

elif idade < 65 and doenca_infectocontagiosa == 'SIM':
     print('O (a) paciente ' + nome + ' deve ser direcionado para sala de espera reservada!')

else:
    print('O (a) paciente ' + nome + ' não tem atendimento prioritário e pode aguardar na sala comum!')

    '''
      PROBLEMA RESOLVIDO
      Se o paciente tiver idade >= 65 e doença contagiosa ele recebe 
atendimento prioritário e vai para sala reservada.

    '''