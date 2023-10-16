# Criando Dicionário

#Dicioário vazio
usuarios = {}
print(usuarios)

# Criando minha primeira lista dentro do dicionário
usuarios = {
   'chaves': ['chaves do 8', '24/12/2022', 'Recep_01'],
   'Quico': ['Quico das Flores', '20/12/2022', 'Raiox_03']    
}
print(usuarios)

# Vou inserir um novo usuário que chegou depois
# Dessa forma eu crio um novo registro dentro do dicionário
usuarios['Florinda'] = ['Dona Florinda', '24/12/2022', 'Raiox_01']
print(usuarios)
print('')
print('*****************************************************************************************')

# Como resgato essas informações, por exemplo: Se eu quiser saber dos acessos do Quico...
print(usuarios.get('Quico'))
