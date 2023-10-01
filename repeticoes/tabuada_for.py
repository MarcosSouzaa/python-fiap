# TABUADA
# ( 0 => INÍCIO,   11 => FIM,    1 => INCREMENTO)

tabuada = int(input('Digite um número para exibir a tabuada: '))
print('Tabuada do número ', tabuada)
for valor in range(0,11,1):
    print(str(tabuada) + ' X ' + str(valor) + ' = ' + str((tabuada*valor)))
