



import os
os.system

nota1 = float(input("digite a primera nota: "))

while nota1 < 0 or nota1 > 10:
    print("A nota deve ser entre 0 e 10 tente novamente")
    nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    print("A nota deve ser entre 0 e 10 tente novamente")
    nota2=float(input("digite a segunda nota"))
nota3 = float(input("digite a terceira nota 3: "))
while nota3 < 0 or nota3 > 10:
    print("A nota deve ser entre 0 e 10 tente novamente")
    nota3 = float(input("digite a terceira nota."))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print("aprovado")
elif 5 <= media < 7:
    print("recuperação")
else:
    print("reprovado")    
    
                    