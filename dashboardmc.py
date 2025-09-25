import streamlit as st
import pandas as pd

# --- Links das planilhas publicadas ---
SITE_INFO_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0l6DdjIIyiCK6MVUkzMWlFVX7N3cw1709MA5Mg13AHe2Gt71Xy_KQm2zHMpUP-DYCk7dSRqT8B4jh/pub?gid=543934944&single=true&output=csv"
TECHNICIAN_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0l6DdjIIyiCK6MVUkzMWlFVX7N3cw1709MA5Mg13AHe2Gt71Xy_KQm2zHMpUP-DYCk7dSRqT8B4jh/pub?gid=1619803162&single=true&output=csv"
FOLLOW_UP_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0l6DdjIIyiCK6MVUkzMWlFVX7N3cw1709MA5Mg13AHe2Gt71Xy_KQm2zHMpUP-DYCk7dSRqT8B4jh/pub?gid=1627559414&single=true&output=csv"

# --- Carregar dados com cache para performance ---
@st.cache_data
def load_data():
    site_info = pd.read_csv(SITE_INFO_URL)
    technician = pd.read_csv(TECHNICIAN_URL)
    follow_up = pd.read_csv(FOLLOW_UP_URL)
    return site_info, technician, follow_up


# --- Carrega os dados ---
site_info, technician, follow_up = load_data()

# --- Interface principal ---
st.title("📊 Blade Repair Dashboard")

tabs = st.tabs(["Site Info", "Technician", "Follow Up"])

with tabs[0]:
    st.subheader("Site Info")
    st.dataframe(site_info)

with tabs[1]:
    st.subheader("Technician")
    st.dataframe(technician)

with tabs[2]:
    st.subheader("Follow Up")
    st.dataframe(follow_up)



