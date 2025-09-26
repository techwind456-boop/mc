import streamlit as st
import pandas as pd

# URLs das planilhas CSV
TECHNICIAN_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0l6DdjIIyiCK6MVUkzMWlFVX7N3cw1709MA5Mg13AHe2Gt71Xy_KQm2zHMpUP-DYCk7dSRqT8B4jh/pub?gid=1619803162&single=true&output=csv"
FOLLOW_UP_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0l6DdjIIyiCK6MVUkzMWlFVX7N3cw1709MA5Mg13AHe2Gt71Xy_KQm2zHMpUP-DYCk7dSRqT8B4jh/pub?gid=1627559414&single=true&output=csv"

# --- Carrega os dados sempre que a página é aberta/atualizada ---
def load_data():
    technician = pd.read_csv(TECHNICIAN_URL)
    follow_up = pd.read_csv(FOLLOW_UP_URL)
    return technician, follow_up

# --- Carrega os dados ---
technician, follow_up = load_data()

# --- Interface ---
st.title("📊 Blade Repair Dashboard")

st.subheader("Technician")
st.dataframe(technician)

st.subheader("Follow Up")
st.dataframe(follow_up)