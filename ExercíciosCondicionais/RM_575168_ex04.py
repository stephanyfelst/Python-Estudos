print ("Escoha o tipo de investimento:\n 1.CDB\n 2.LCI\n 3.LCA")
tipo_investimento = int(input("Digite a opção desejada: "))

if tipo_investimento < 1 or tipo_investimento > 3:
    print ("A opção inserida é inválida.")
else:
    valor_resgate = int(input("Informe o valor do resgate: "))
    dias_aplicados = int(input("Informe os dias de aplicação: "))

    if dias_aplicados <= 180:
        aliquota = 22.5
    elif dias_aplicados <= 360:
        aliquota = 20
    elif dias_aplicados <= 720:
        aliquota = 17.5
    else:
        aliquota = 15

    if tipo_investimento == 1:
        valor_ir = valor_resgate * (aliquota / 100)
        print (f"O valor do imposto de renda a ser pago é: R${valor_ir:.2f}")
    else:
        print ("O investimento selecionado é isento de Imposto de Renda.")    



