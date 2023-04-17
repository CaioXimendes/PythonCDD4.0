tipo_combustivel = input("Qual o tipo de Combustível você abasteceu o carro?\n Digite G para gasolina\n Digite E para etanol\n")
preco_porlitro_gasolina = 5.8
preco_porlitro_etanol = 4.9
if tipo_combustivel == "G" or tipo_combustivel == "g" or tipo_combustivel == "E" or tipo_combustivel == "e":
    if tipo_combustivel in "Gg":
        litros_vendidos = float(input(f"Informe a quantidade de litros vendidos de {tipo_combustivel}: \n"))
        valor_pago_cliente = litros_vendidos * preco_porlitro_gasolina
        print(f"O valor pago de Gasolina pelo cliente foi de: R$ {valor_pago_cliente}")
    elif tipo_combustivel in "Ee":
        litros_vendidos = float(input(f"Informe a quantidade de litros vendidos de {tipo_combustivel}: \n"))
        valor_pago_cliente = litros_vendidos * preco_porlitro_etanol
        print(f"O valor pago de Etanol pelo cliente foi de: R$ {valor_pago_cliente}")
else:
    print("Combustivel nao reconhecido!")
