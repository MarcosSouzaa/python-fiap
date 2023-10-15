# WHILE - DESAFIO

resposta = 'SIM'
while resposta == 'SIM':

    nome = input('Digite seu nome: \n').upper() 

    print('Niveis de acesso: ADM(administrador), USR(usuário), GUEST(visitante)')  
    
    nivel = input('Digite o nível de acesso: \n').upper()

    if nivel == 'ADM' or nivel == 'USR':
        genero = input('Digite seu gênero: \n').upper()
        if nivel == 'ADM':
            if genero == 'FEMININO':
                print('Olá administradora ' + nome)
            else:
                print('Olá administrador ' + nome)
        else:
            if nivel == 'USR':
                if genero == 'FEMININO':
                    print('Olá usuária ' + nome)
                else:
                    print('Olá usuário ' + nome)

    elif nivel == 'GUEST':
        print('Olá visitante!')
    else:
        print('Olá desconhecido!')                   
resposta = input('digite SIM para continuar: ').upper()

