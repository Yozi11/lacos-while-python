import streamlit as st

st.title("faça seu login")
st.header("cadastro")


login_correto = "juan123"
senha_correta = "123"

st.session_state.setdefault("desabilitar",False)
st.session_state.setdefault("tentativas",0)

login = st.text_input("digite seu login: ", disabled=st.session_state.desabilitar)
senha = st.text_input("digite sua senha: ", type="password",disabled=st.session_state.desabilitar )



if st.button("entrar"):
    if login == login_correto and senha == senha_correta:
        st.success("login com sucesso")
    else:
        st.session_state.tentativas += 1
        if st.session_state.tentativas <= 3:

            st.error(f"login sem invalido, tentativas: {st.session_state.tentativas}")
        else:
            st.session_state.desabilitar = True    
                      
