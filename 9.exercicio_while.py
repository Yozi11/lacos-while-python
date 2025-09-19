numeros_impares = 0
numeros_pares = 0
soma_pares = 0
soma_geral = 0
contador_geral = 0



while True:
    numero_str =input("digite um numero: ")
    numero = int(numero_str)

    if numero == 0:
        break
    if numero < 0:
        print("numero negativos. apenas positivos")
        continue
    contador_geral += 1
    soma_geral += numero

    if numero % 2 == 0:
        numeros_pares += 1
        soma_pares += numero
    else:
        numeros_impares += 1

if contador_geral > 0:
    print(f"numeros pares{numeros_pares} ")
    print(f"numero impares{numeros_impares}")
    if numeros_pares > 0:
        media_pares = soma_pares / numeros_pares
        print(f"valor do numeros pares{numeros_pares:.2f}")
    else:
        print("nenhum valor inserido")
    media_geral = soma_geral / contador_geral
    print(f"media geral de todos: {media_geral}")
else:
    print("nenhum numero positivos")            
              
          


    

    


