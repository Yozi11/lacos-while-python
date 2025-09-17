import streamlit as st

st.title("laço de repetição.while")

st.write("crie um programa que solicite ao usuario seu login e uma senha.O programa deve solicitar o login e senha apenas três vezes. Caso ultrapasse o número de tentativas, o programa deve ser finalizado.")


login_salvo = "Marta" 
senha_salva = "123"
#variaveis internas do streamlit
st.session_state.setdefault("campo",False)
st.session_state.setdefault("tentativas",0)

login = st.text_input("digite seu login: ",disabled=st.session_state.campo)
senha = st.text_input("digite sua senha: ",type="password",disabled=st.session_state.campo)

if st.button("verificar"):
    if login == login_salvo and senha == senha_salva:
        st.success("bem-vindo")
    else:
        st.session_state.tentativas += 1
        if st.session_state.tentativas <= 3:
            st.warning(f"login ou senha invalida")

        
            st.error(f"login sem invalido, tentativas: {st.session_state.tentativas}")
        else:
            st.session_state.desabilitar = True

    
    
       
                
