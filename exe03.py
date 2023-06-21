def calcular_desconto(idade):
    if idade < 21:
        desconto = 0.15
        print("Você terá desconto de 15%")
    else:
        desconto = 0.10
        print("Você terá desconto de 10%")

    return desconto

def calcular_valor_com_desconto(valor, desconto):
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto


idade_cliente = int(input("Digite a idade: "))
valor_compra = float(input("Digite o valor da compra: "))

desconto_aplicado = calcular_desconto(idade_cliente)
valor_com_desconto = calcular_valor_com_desconto(valor_compra, desconto_aplicado)

print("O valor da compra é R$ = {} com desconto é: R$ = {:.2f}".format(valor_compra, valor_com_desconto))
