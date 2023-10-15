# Decisões
nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
if idade >= 65:
    print('O paciente ' + nome + ' possui atendimento Prioritário!')
else:
    print('O paciente ' + nome + ' não possui atendimento prioritário!')

print('FIM') # Esse print est´fora do if, então sempre será impresso!