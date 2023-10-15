# Exercício com Variáveis
'''
"Declaro para o senhor Gonçalves Dias que o senhor Humberto Delgado esteve presente
no evento SecurityCup e gastou o valor de R$30,00 com entrada"

'''
nome1 = input('Para quem vai a declaração? R= ')
nome2 = input('Quem esteve presente? R= ')
evento = input('Qual o nome do evento? R= ')
vlr_entrada = float(input('Qual o valor da entrada? R= '))

print('"Declaro para o senhor ' + nome1 + ' que o senhor ' +
       nome2 + ' \n esteve presente no evento ' + evento +
      ' e gastou o valor de R$' + str(vlr_entrada) + ' com entrada."')