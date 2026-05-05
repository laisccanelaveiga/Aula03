# Compra acima 250 aplicar 16% de desconto

valor = float(input("Digite o valor da compra: "))

if valor > 250:
    valor -= (valor * 0.16)
    print(f'O valor à pagar após desconto é de R$ {valor:.2f}')

else:
    print(f"Valor à pagar: R$ {valor:.2f}")
