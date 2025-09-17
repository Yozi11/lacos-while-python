import os
os.system("cls")

login_correto ="juanzitos"
senha_correta ="1234"
tentativa = 0

while tentativa < 3:
    login = input("digite seu login: ")
    senha = input("digite sua senha: ")

    if login == login_correto and senha == senha_correta:
        print("login correto")
        break
    else:
        tentativa += 1
        print(f"tentativa{tentativa} de 3.")

     # Se o usuário já tentou 3 vezes, o código será finalizado
        if tentativa == 3:
            print("voce atingiu o maximo de tentativas")    






