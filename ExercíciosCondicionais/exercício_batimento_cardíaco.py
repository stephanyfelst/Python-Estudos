#Verificar se os batimentos cardíacos por minuto se encontram na faixa adequada. Para isso, você deve solicitar ao usuário que informe o seu número de batimentos por minuto (BPM) e a idade. A partir disso, o script deve verificar e exibir uma mensagem informando se os batimentos do usuário encontram-se dentro da faixa adequada,acima da faixa adequada ou abaixo da faixa adequada.

idade_usuario = int(input("Insira a sua idade: "))
bpm_usuario = float(input("Insira o seu Batimento Cardíaco por minuto (BPM): "))

adequado = False

if idade_usuario <= 2:
    adequado = bpm_usuario >= 120 and bpm_usuario <= 140
        
elif idade_usuario >= 8 and idade_usuario <= 17:
    adequado = bpm_usuario >= 80 and bpm_usuario <= 100

elif idade_usuario >= 18 and idade_usuario <= 65:
    adequado = bpm_usuario >= 70 and bpm_usuario <=100

elif idade_usuario > 65:
    adequado = bpm_usuario >= 50 and bpm_usuario <= 60

if adequado:
    print ("Seus batimentos cardíacos estão dentro da faixa adequada.")
    
else: print("Seus batimentos cardíacos estão fora da faixa adequada.")


    

    



