# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno_escolar = input ("Digite qual o seu turno escolar (M-matutino, V-vespertino ou N-noturno): ")

match turno_escolar.upper():
    case "M":
        print ('Bom dia!')
    case "V":
        print ("Boa tarde!")
    case "N":
        print ("Boa noite!")
    case _:
        print ("Valor inválido")