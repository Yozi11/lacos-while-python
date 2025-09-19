import os
os.system("cls")



valor_total = 0
continuar = "s"

print("Bem vindo ao restaurante ")

#loop para o usuario digitar "S" ou "s"
while continuar.lower() == "s":

    # Mostrar o cardapio
    print("\n---Cardapio--")
    print("Codigo |  Prato | Valor")
    print("1   |Picanha |R$ 25,00 ")
    print("2  |Lasanha | 20,00")
    print("3 |Strogonoff |18,00")
    print("4 |Bife Acebolado|15,00")
    print("5 |pão com ovo|5,00")

    codigo = input("digite o codigo do prato desejado: ")

    if codigo.isdigit():
        codigo = int(codigo)
        if codigo == 1:
            valor_total+= 25.00
            print("picanha adicionada")
        elif codigo == 2:
            valor_total+= 20.00
            print("Lasanha adicionada")
        elif codigo == 3:
            valor_total+= 18.00
            print("strogonoff adicionado")
        elif codigo == 4:
            valor_total+= 15.00
            print("Bife Acebolado adicionado")
        elif codigo == 5:
            valor_total+= 5.00
            print("pão com ovo adicionado")
        else:
            print("codigo invalido.")

          
    else:
        print("entrada invalida")
    # Perguntar se o usuario deseja mais alguma coisa.
    print(f"\nsubtotal: R$ {valor_total:.2f}")
    continuar = input("Deseja escolher outro prato (S/n): ")
#Loop finalizado
print("\n pedido finalizado")
print(f"O valor total a ser pago e: R${valor_total:.2f}")
print("volte sempre")    
                                     