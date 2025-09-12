import os
os.system


QUANTIDADE_NOTAS = 2
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = int(input(f"digite a {i+1} nota: "))
        if nota >= 0 and nota <= 10:
            break
    
        soma = soma + nota

media = soma / QUANTIDADE_NOTAS
print(f"media:{media}")            