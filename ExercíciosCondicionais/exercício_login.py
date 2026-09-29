#Peça: Usuário e Senha | Permita acesso apenas se ambos estiverem corretos.

print ("LOGIN")
print (" ")


usuario = input ("Crie um e-mail de acesso: ")
senha = input ("Crie uma senha de acesso: ")

login_usuario = input ("Digite o e-mail cadastrado: ")
senha_login = input ("Digite a sua senha: ")

if usuario == login_usuario and senha == senha_login:
    print ("Login realizado com sucesso!")

else:
    print ("Os dados inseridos são inválidos.") 

# Testando not in, isdigit e LEN

print ("LOGIN")
print (" ")

usuario = input ("Crie um e-mail de acesso: ")
if "@" not in usuario or ".com" not in usuario:
    print ("E-mail inválido.")
else:
    senha = input ("Crie uma senha de acesso: ")
    if senha.isdigit() and len(senha) == 6:

        login_usuario = input ("Digite o e-mail cadastrado: ")
        senha_login = input ("Digite a sua senha: ")

        if usuario == login_usuario and senha == senha_login:
            print ("Login realizado com sucesso!")
        else:
            print ("Os dados inseridos são inválidos.")
    else:
        print ("A senha precisa possuir 6 digitos. Por favor, insira uma nova senha.")

    
