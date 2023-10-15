# Identificação de funções -  def => definição

# função para preencher a lista com os dados que desejo
def preencherInventario(lista):
    resp = 'S'
    while resp == 'S':
        equipamento = [input('Equipamento: ').upper(),
                       float(input('Valor: ')),
                       int(input('Número serial')),
                       input('Departamento: ').upper()]
        lista.append(equipamento)
        resp = input('Digite "S" para continuar: ')

''' A função “exibirInventario()”irá receber a lista, por parâmetro, e, então,
executará o laço “for” para exibir os dados da lista recebida.'''
def exibirInventario(lista):
    for elemento in lista:
        print('Nome..............:', elemento[0])
        print('Valor.............:', elemento[1])
        print('Serial............:', elemento[2])
        print('Departamento......:', elemento[3])

'''A função acima não apresentou nenhuma novidade: recebe a lista, solicita o 
nome a ser pesquisado, localiza o nome do produto na lista e, se for encontrado, irá 
exibir os dados do elemento localizado'''
def localizarPorNome(lista):
    busca = input('\nDigite o nome do equipamento que deseja encontrar: ')
    for elemento in lista:
        if busca == elemento[0]:
            print('Valor......:', elemento[1])
            print('Serial.....:', elemento[2])

'''A função depreciarPorNome() apresenta dois parâmetros: um deles é a lista 
na qual estão os equipamentos que sofrerão a depreciação; e o outro é a 
porcentagem que se deseja depreciar. Repare que a fórmula matemática foi alterada 
quando comparada com o arquivo anterior'''
def depreciarPorNome(lista, porc):
    depreciacao = input('\nDigite o nome do equipamento que será depreciado: ')
    for elemento in lista:
        if depreciacao == elemento[0]:
            print('Valor antigo: ', elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print('Novo valor: ', elemento[1])

'''A função excluirPorSerial() retorna uma string, ou seja, quando formos 
chamar essa função, devemos fazê-la dentro de um comando print(), para que 
possamos ver a mensagem.'''
def excluirPorSerial(lista):
    serial = int(input('\nDigite o serialdo equipamento que será excluido: '))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return 'Itens excluídos'

'''E para finalizar, a função resumirValores() poderia ser facilmente dividida em 
três funções: somar(), exibirMaiorValor() e exibirMenorValor(), tudo depende muito 
do contexto e da especificação que se deseja obter. Para o nosso exemplo, 
manteremos apenas como uma função que realiza as três tarefas.'''
def resumirValores(lista):
    elemento = []
    for valores in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print('O equipamento mais caro custa: ', max(valores))
        print('O equipamento mais barato custa: ', min(valores))
        print('O total de equipamentos é de: ', sum(valores))
