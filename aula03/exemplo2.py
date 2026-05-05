# idade = int(input("Digite dua idade: "))
# if idade >= 18:
#     print("Maior de idade")
# else:
#     print("Menor de idade")
# --------------------------------------------------------------------------------

# Classificação por pontos
pontos = int(input("Informe os pontos: "))
if pontos >= 100:
    total_pontos = pontos + 10
    print(f"Excelente! Agora você tem {total_pontos} pontos.")

elif pontos >= 50:
    total_pontos = pontos + 5
    print(f"Bom desempenho! Agora você tem {total_pontos} pontos.")

else:
    print(f"Você não atingiu a meta par bônus, fez {pontos} pontos")

print("\nFim\n")



