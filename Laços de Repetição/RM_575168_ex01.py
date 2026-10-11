segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

quantidade = int(input("Informe o número de colaboradores: "))

for i in range(quantidade):
    dia = input("Informe o dia de sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira ou sexta-feira): ").lower()

    if dia == "segunda" or dia == "segunda-feira":
        segunda += 1
    elif dia == "terça-feira" or dia == "terça" or dia == "terca":  
        terca += 1
    elif dia == "quarta" or dia == "quarta-feira":
        quarta += 1
    elif dia == "quinta" or dia == "quinta-feira":
        quinta += 1
    elif dia == "sexta" or dia == "sexta-feira":
        sexta += 1

maior = 0
dia_escolhido = ""
if segunda > maior:
    maior = segunda
    dia_escolhido = "segunda" or dia == "segunda-feira"
if terca > maior:
    maior = terca
    dia_escolhido = "terça-feira" or dia == "terça" or dia == "terca"
if quarta > maior:
    maior = quarta
    dia_escolhido = "quarta" or dia == "quarta-feira"
if quinta > maior:
    maior = quinta
    dia_escolhido = "quinta" or dia == "quinta-feira"
if sexta > maior:
    maior = sexta
    dia_escolhido = "sexta" or dia == "sexta-feira"

empate = 0

if segunda == maior:
    empate += 1
if terca == maior:
    empate += 1
if quarta == maior:
    empate += 1
if quinta == maior:
    empate += 1
if sexta == maior:
    empate += 1
if empate > 1:
    print ("Houve empate")
else:
    print (f"O dia escolhido pelos colaboradores é: {dia_escolhido}")
    print (f"Total de votos: {maior}")    
