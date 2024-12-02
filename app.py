import streamlit as st
import sqlite3

# Função para verificar o login no banco de dados
def check_login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Verifica as credenciais no banco de dados
    cursor.execute('''
    SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    user = cursor.fetchone()
    
    conn.close()
    return user is not None

# Interface do Streamlit
def login_page():
    st.title("Login")

    # Entradas de usuário
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    # Botão de login
    if st.button("Entrar"):
        if check_login(username, password):
            st.success("Login bem-sucedido!")
            st.write("Bem-vindo(a),", username)
        else:
            st.error("Usuário ou senha incorretos.")

if __name__ == "__main__":
    login_page()
