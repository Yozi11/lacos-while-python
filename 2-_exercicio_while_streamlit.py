import streamlit as st

def pedir_nota(nome_nota):
    while True:
        nota = st.number_input(f"Digite a {nome_nota} (0 a 10):", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
        # Como number_input já limita, só precisamos do valor
        return nota

def main():
    st.title("Calculadora de Média do Aluno")

    st.write("Informe as notas do aluno (de 0 a 10):")

    nota1 = pedir_nota("primeira nota")
    nota2 = pedir_nota("segunda nota")

    media = (nota1 + nota2) / 2
    st.success(f"A média do aluno é: {media:.2f}")

if __name__ == "__main__":
    main()
