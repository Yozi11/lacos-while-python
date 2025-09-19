import os
os.system

soma = 0
quantidade_numeros = 0

while True:
    numero = int(input("digite uma nota"))
   
    if numero < 0:
        break
    quantidade_nota += 1
    soma += numero
media = soma / quantidade_numeros

print(f"\nmedia:{media}")

