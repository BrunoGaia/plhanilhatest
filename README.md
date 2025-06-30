# Streamlit + Google Sheets Visitor Log

Este app simples em Python com Streamlit salva o nome e a idade de quem acessa em uma planilha do Google Sheets.

## ✅ Pré-requisitos

- Conta no Google Cloud com uma Service Account.
- Planilha criada no Google Sheets.
- Compartilhar a planilha com a conta de serviço (ex: `xxxx@xxxx.iam.gserviceaccount.com`).

## 🔧 Instalação

```bash
git clone https://github.com/seu-usuario/streamlit-gsheets-app.git
cd streamlit-gsheets-app
pip install -r requirements.txt
```

Adicione sua credencial no caminho `credenciais/calcunip-7ca1152065d4.json`.

## 🚀 Execução

```bash
streamlit run app.py
```

## 🛑 Importante

**NÃO** suba seu arquivo JSON de credenciais no GitHub público!
