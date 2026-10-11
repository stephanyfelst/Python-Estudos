# Valor a vista
valor_carro = int(input("Por gentileza, informe o valor do carro (sem pontos): "))
desconto = valor_carro * 0.20
desconto_carro = valor_carro - desconto

print (" ")
print (f"O preço final á vista com desconto de 20% é de R${desconto_carro:.2f}")
print (" ")

# Parcelas
print ("TABELA DE VALORES PARCELADO")
print ("-----------------")

for parcelas in range(6,61,6):
    juros = (parcelas // 6) * 3

    valor_final = valor_carro * (1 + juros / 100)
    valor_parcelas = valor_final / parcelas

    print (f"O preço final parcelado em {parcelas}x é de R${valor_final:.2f} com parcelas de R${valor_parcelas:.2f}")