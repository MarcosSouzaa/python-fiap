# TRABALHANDO COM FOR
'''
Para o comando 'for', criamos uma variável chamada 'numero'e dizemos que, de acordo 
de acordo com a função 'range()' que permite especificar uma faixa de valores e como será 
incrementada, a variável iniciará com o valor 1 até o valor qu for digitado pelo usuário
final. E esta faixa será incrementada de 1 em 1, conforme o último valor especificado
dentro da função range(). O conteúdo do for será repetido enquanto não atingir o valor 
máximo que foi digitado pelo usuário final.

'''
for numero in range(0, int(input('Digite um número para determinar o fim: ')), 1):
    print(' ' + str(numero))