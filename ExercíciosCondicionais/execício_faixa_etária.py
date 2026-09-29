#Receba a idade de uma pessoa e classifique:

#Criança: até 12 anos
#Adolescente: 13 a 17 anos
#Adulto: 18 a 59 anos
#Idoso: 60 anos ou mais

print ("FAIXA ETÁRIA DO USUÁRIO")
print (" ")
try:
    idade = int(input ("Digite a sua idade: "))

    if idade <= 12:
        print ("Criança")
    elif idade <=17:
        print ("Adolescente")
    elif idade >= 18 and idade <= 59:
        print ("Adulto")
    else:
        print ("Idoso")
except ValueError:
    print ("O dado inserido é inválido! Por gentileza, insira apenas números.")



