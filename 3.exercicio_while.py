#Crie um programa que solicite ao usuário seu login e uma senha
#O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. 




login_correto = "usuario123"
senha_correta = "senha123"


while True:
 
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
   
    if login == login_correto and senha == senha_correta:
        print("Login bem-sucedido!")
        break  
    else:
        print("Login ou senha incorretos. Tente novamente.")
