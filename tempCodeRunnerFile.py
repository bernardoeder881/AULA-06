resposta = 'S'
valor = 0
desconto = 0
valortotal = 0

while resposta != 'N':
  valor = int(input('Informe o valor do produto: '))
  if valor > 1000:
      desconto = valor * 0.1
      valorvenda = valor - desconto
      print(f'Valor da venda = R${valor}')
      print(f'Valor do desconto = R${desconto}')
      print(f'Valor a pagar = R${valorvenda}')
  else:
    desconto = 0
    valorvenda = valor - desconto
    print(f'Valor a pagar = R${valorvenda}')
  valortotal += valorvenda
  print(f' Total parcial = R${valortotal}') 
  resposta = input('Continuar S ou N?').upper().strip()
    while resposta != 'S':
     resposta = input('Continuar S ou N?').upper().strip() 
print("Venda finalizada")
print(f'Valor Total de R$ {valortotal}') 