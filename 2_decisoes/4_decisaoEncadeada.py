# DECISÃO ENCADEADA
'''
 Caso 2: Mulheres grávidas também são consideradas para o atendimento prioritário
  (sala BRANCA ou AMARELA). Você vai perguntar para todos os pacientes se eles 
  estão grávidos? Não! Apenas para as mulheres. Perguntaria para todas as mulheres?
  Não precisaria perguntar para as mulheres com idade igual ou superior a 65 anos,
  e descartar crianças com menos de 10 anos.
'''
# Ao invés de usarmos DECISÃO COMPOSTA, usaremos DECISÃO ENCADEADA

nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
doenca_infectocontagiosa = input('Suspeita de doença infectocontagiosa? ').upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa == 'SIM':
    print('Encaminhe o paciente para sala AMARELA!')
elif doenca_infectocontagiosa == 'NÃO':
    print('Encaminhe o paciente para sala Branca! ')
else:
    print('Responda a suspeita de doença infectocontagiosa com SIM ou NÃO.')

    # SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print('Paciente com prioridade!')
else:
    genero = input("Digite o gênero do paciente: ").upper()
    if genero == 'FEMININO' and idade > 1:
        gravidez = input('A paciente está grávida? ').upper()
        if gravidez == 'SIM':
            print('Paciente COM prioridade!')
        else:
            print('Paciente SEM prioridade!')
    else:
        print('Paciente SEM prioridade!') 
