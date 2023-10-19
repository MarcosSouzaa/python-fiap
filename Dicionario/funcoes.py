def perguntar():
    return('O que deseja perguntar?\n' +
           '<I> - Para Inserir um usuário\n' +
           '<P> - Para Pesquisar um usuário\n' +
           '<E> - Para Excluir um usuário\n' +
           '<L> - Para listar um usuario: ').upper()

def inserir(dicionario):
    dicionario[input('Digite o login: ').upper()] = [input('Digite o nome: ').upper(),
                                                     input('Digite a última data de acesso: '),
                                                     input('Qual a última estação acessada: ').upper()]
    
def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print('Nome............: ' + lista[0])
        print('Ultimo acesso...: ' + lista[1])
        print('Ultima estação..: ' + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!= None:
        del dicionario[chave]
        print('Objeto Eliminado')

def listar(dicionario):
    for chave, valor, in dicionario.items():
        print('Objeto......')
        print('Login', chave)
        print('Dados', valor)