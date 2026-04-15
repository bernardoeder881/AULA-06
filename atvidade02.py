resposta = 'S'
valor = 0
desconto = 0

while resposta != 'N':
    valor = int(input('Informe o valor da venda: '))
    if valor > 1000:
        desconto = valor * 0.1
        valorfinal = valor - desconto
        print(f'Valor da venda = R${valor}')
        print(f'Valor do desconto = R${desconto}')
        print(f'Valor a pagar = R${valorfinal}')
    else:
       print(f'Valor a pagar = R${valor}')
     
    resposta = input('Continuar S ou N?').upper().strip()
    
print("Venda finalizada")


   