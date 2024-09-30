'''
# ForLoop para numeros

for numero in range(1, 20, 2):
    print(numero)
    

    # ForLoop para Strings

for letra in 'Google':
    print(letra)

palavra = 'Google Sheets'

for letra2 in palavra:
    print(letra2)
   

    #For loop com if e else

compra_efetuada = true
dados_compra = 'Compra no valor de R$12,50 e entrega confirmada'

for enviar in range(3):
    if compra_efetuada:
        print(dados_compra)
        print('Detalhes enviado para seu email')
        break
else:
    print('Falha na compra')
    

#NESTED LOOPS

for numero1 in range(1,6):
    print('Produto ' +str(numero1))
    for numero2 in range(5):
        print(numero1, numero2)



#Separando Strings

palavra = 'FANTASTICO'

for space in palavra:
    print(space + ' ', end='')
    


#Criando um quadrado

linhas = 6
colunas =6 
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()
    '''


#Conhecendo o WHILE LOOP

valor = 100
dia = 0
while valor > 20:
    dia += 1
    print(f' No dia {dia} o produto vai ser vendido por R${valor}' )
    valor -= 5