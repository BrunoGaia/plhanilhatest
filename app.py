import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import json

# --- Autenticação via secrets ---
service_account_info = json.loads(st.secrets["gcp_service_account"])
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
credentials = Credentials.from_service_account_info(service_account_info, scopes=scopes)
client = gspread.authorize(credentials)

# --- Configuração da planilha ---
SHEET_ID = "1xK8B8cKWgmt8E2H6QlnASR336ZkTGsVAXX0_Kj9qB0A"
SHEET_NAME = "planilha teste"

sheet = client.open_by_key(SHEET_ID)
worksheet = sheet.worksheet(SHEET_NAME)

# --- Interface do usuário ---
st.title("Registro de Visitantes")

nome = st.text_input("Digite seu nome:")
idade = st.number_input("Digite sua idade:", min_value=0, max_value=120, step=1)

if st.button("Enviar"):
    if nome:
        worksheet.append_row([nome, idade])
        st.success(f"Obrigado pela visita, {nome}!")
    else:
        st.warning("Preencha todos os campos.")

# --- Mostrar dados registrados ---
st.subheader("Visitantes Registrados:")
dados = worksheet.get_all_values()
df = pd.DataFrame(dados[1:], columns=dados[0])  # Ignora cabeçalho duplicado
st.dataframe(df)
