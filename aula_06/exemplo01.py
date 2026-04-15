# Calcular média
# n1 = float(input('Nota 1: ')) 
# n2 = float(input('Nota 2: '))
# media = (n1 + n2)/2
# print(media)
 
#Estrutura de repetição (FOR)

#for i in range(5):
    #print(i)
#---------------------------
# qtd = 31
# for i in range(qtd):
#     print(i)
# #---------------------------
# qtd = 31
# for i in range(qtd):
#     print(i, end = " ")# imprime na mesma linha
#-------------------------------------------

usuario = ""


# for u in range(3):
#     if u == 0:
#         usuario = "Eder"
#     elif u==1:
#         usuario = "Fernando"
#     print(f'\nUsuário {usuario}')
#     num1 = int(input('Inserir o número 1: '))
#     num2 = int(input('Inserir o número 2: '))
#     soma = num1 + num2
#     print(f'O total é {soma}.')
#------------------------------------------------
#Variável acuuladora
# soma = 0
# for u in range(5):
#     if u == 0:
#         usuario = "Eder"
#     elif u==1:
#         usuario = "Fernando"
#     else:
#         usuario = "desconhecido"

#     print(f'\nUsuário {usuario}')
#     numero = float(input('Digite o número: '))
#     soma = soma + numero
#     print(f'O total é {soma}.')

soma = 0

for v in range(5):
    venda = float(input('\nInforma o valor:'))
    if venda > 100:
        soma += venda #soma = soma + venda
        print(f'Valor R$ {venda} soamdo')
        print(f'Total de R$ {soma}')
    else:
        print('Valor não computado' )
        print(f'Total de R$ {soma}')
print(f'\nTotal de R$ {soma}')