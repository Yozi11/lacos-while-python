import os
os.system("cls")



#escreva um algoritmo que solicite ao usuario a nota de um aluno
#caso seja menor que 0 ou maior que 10, mostre a pergunta novamente
# mostre a nota infromada pelo usuario
while True:
    nota = int(input("digite a nota: "))
    if nota >= 0 or nota <= 10:
        break


    
print(f"nota: {nota}")    
