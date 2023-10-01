# DESAFIO
'''
o módulo solicitará o nível de acesso de uma pessoa que pode ser: ADM, USR ou GUEST e
o gênero dessa pessoa. Caso o nível seja ADM, ele deverá exibir: " Olá administrador"
para homens ou " Olá administradora" para mulheres. 
Se o nivel for USR, deverá exibir "Olá usuário" para homens ou olá "usuária" para mulheres.
Se o nível for GUEST, a mensagem deverá ser "Olá visitante".
Se o nível digitado for diferente de ADM, USR ou GUEST deverá exibr a mensagem " Olá Desconhecido".
Considere apenas os gêneros masculino e feminino. 

'''
nome = input('Digite seu nome: ').upper()
genero = input('Digite seu gênero: ').upper()

nivel_acesso = input('Escolha o nível de acesso: ADM (administrador), USR (usuário) ou GUEST (visitante):\n ').upper()
print('')
if nivel_acesso == 'ADM':
    if genero == 'MASCULINO':
        print("Olá administrador " + nome)
    else:
        print('Olá administradora ' + nome)  

elif nivel_acesso == 'USR':
    if genero == 'MASCULINO':
        print('Olá usuário ' + nome)
    else:
        print('Olá usuária ' + nome)

elif nivel_acesso == 'GUEST':
    if genero == 'MASCULINO':
        print('Olá visitante ' + nome)
    else:
        print('Olá amiga visitante ' + nome)

else:
    print('" Olá Desconhecido! "')
