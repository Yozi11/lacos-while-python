import os
os.system("cls")
salarios = []
crianças = []

while True:
    print("Código | Descrição")
    print("  1    | Adicionar família")
    print("  2    | Sair e exibir resultados")
    opc = input("Escolha (1-2): ").strip()

    if opc == '1':
        # ler salário (aceita vírgula ou ponto como decimal; sem separador de milhares)
        while True:
            s = input("Salário (ex: 2500.50 ou 2500,50): ").strip().replace(',', '.')
            if s.count('.') <= 1 and s.replace('.', '', 1).isdigit():
                salario = float(s)
                if salario >= 0:
                    break
            print("Entrada inválida. Digite um salário válido (número não negativo).")

        # ler número de filhos (inteiro não negativo)
        while True:
            f = input("Número de filhos: ").strip()
            if f.isdigit():
                filhos = int(f)
                break
            print("Entrada inválida. Digite um número inteiro não negativo para filhos.")

        salarios.append(salario)
        crianças.append(filhos)
        print("Família adicionada com sucesso!\n")

    elif opc == '2':
        # sair e exibir resultados
        break

    else:
        print("Opção inválida. Digite 1 ou 2.\n")

# Exibir resultados
if len(salarios) == 0:
    print("\nNenhuma família cadastrada.")
else:
    total_familias = len(salarios)
    media_salario = sum(salarios) / total_familias
    media_filhos = sum(crianças) / total_familias
    maior_salario = max(salarios)
    menor_salario = min(salarios)

    print("\nResultados da pesquisa:")
    print(f"- Total de famílias que responderam: {total_familias}")
    print(f"- Média do salário da população: R$ {media_salario:,.2f}")
    print(f"- Média do número de filhos: {media_filhos:.2f}")
    print(f"- Maior salário: R$ {maior_salario:,.2f}")
    print(f"- Menor salário: R$ {menor_salario:,.2f}")
