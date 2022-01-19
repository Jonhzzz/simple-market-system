cont = 1
compras = []
valor = 0.0
frutas = ["macã", "banana", "pera", "laranja"]

while cont == 1:

  for i in frutas:
      print(i)

  print("-=" * 20)
  pedido = input("O que você deseja? ")
  quantidade = float(input("Quantas Unidades Deseja?"))
  print(pedido)

  if pedido.lower() in frutas:
    print("-=" * 20)
    print("Obrigada pelo Pedido!")
    compras.append(pedido)
    valor = quantidade * 1.5
  else:
    print("-=" * 20)
    print("Me Desculpe Mas Seu Item Ainda Não Está Disponivel!")

  print("-=" * 20)
  continuar = input("Deseja Mais Alguma Coisa? ")


  if continuar == "sim":
    cont = 1
  else: 
    cont = 0

    print("-=" * 20)

    print("Pedido:")

    print("-=" * 20)
    
    for i in compras:
      print(i)

    print("-=" * 20) 

    print("valor:")

    print("-=" * 20)

    print("R${}".format(valor))

    print("-=" * 20)
