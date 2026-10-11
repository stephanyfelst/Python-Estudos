valor_divida = int(input ("Por gentileza, insira o valor da dívida (sem pontos): "))

for parcelas in range(1,13):
    if parcelas == 1:
        juros = 0 

    elif parcelas == 3:
        juros = 10

    elif parcelas == 6:
        juros = 15

    elif parcelas == 9:
        juros = 20

    elif parcelas == 12:
        juros = 25

    else:
        continue

    valor_juros = valor_divida * (juros / 100)
    valor_total = valor_divida + valor_juros
    valor_parcelas = valor_total / parcelas

    print (" ")
    print (f"TOTAL: R${valor_total:.2f} | JUROS: R${valor_juros:.2f} | NÚMERO DE PARCELAS {parcelas}x | VALOR DA PARCELA: R${valor_parcelas:.2f}")