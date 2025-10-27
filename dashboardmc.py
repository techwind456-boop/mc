import streamlit as st
import pandas as pd

# ---------- CONFIGURAÇÕES ----------
# URLs das planilhas publicadas como CSV
FOLLOW_UP_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0l6DdjIIyiCK6MVUkzMWlFVX7N3cw1709MA5Mg13AHe2Gt71Xy_KQm2zHMpUP-DYCk7dSRqT8B4jh/pub?gid=1627559414&single=true&output=csv"
TECHNICIAN_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0l6DdjIIyiCK6MVUkzMWlFVX7N3cw1709MA5Mg13AHe2Gt71Xy_KQm2zHMpUP-DYCk7dSRqT8B4jh/pub?gid=1619803162&single=true&output=csv"

# ---------- FUNÇÃO PARA CARREGAR DADOS ----------
@st.cache_data
def load_data():
    follow_up = pd.read_csv(FOLLOW_UP_URL)
    technician = pd.read_csv(TECHNICIAN_URL)
    return follow_up, technician

# ---------- INTERFACE ----------
st.set_page_config(page_title="Blade Repair Dashboard", layout="wide")

st.title("📊 Blade Repair Dashboard")

follow_up, technician = load_data()

# ---------- ABAS ----------
tab1, tab2 = st.tabs(["Follow Up", "Technician"])

with tab1:
    st.subheader("Follow Up")
    st.dataframe(follow_up, use_container_width=True)

with tab2:
    st.subheader("Technician")
    st.dataframe(technician, use_container_width=True)


