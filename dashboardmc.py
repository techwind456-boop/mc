import streamlit as st
import pandas as pd

# --- links atualizados ---
SITE_INFO_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0l6DdjIIyiCK6MVUkzMWlFVX7N3cw1709MA5Mg13AHe2Gt71Xy_KQm2zHMpUP-DYCk7dSRqT8B4jh/pub?gid=543934944&single=true&output=csv"
TECHNICIAN_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0l6DdjIIyiCK6MVUkzMWlFVX7N3cw1709MA5Mg13AHe2Gt71Xy_KQm2zHMpUP-DYCk7dSRqT8B4jh/pub?gid=824764180&single=true&output=csv"
FOLLOW_UP_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0l6DdjIIyiCK6MVUkzMWlFVX7N3cw1709MA5Mg13AHe2Gt71Xy_KQm2zHMpUP-DYCk7dSRqT8B4jh/pub?gid=363742714&single=true&output=csv"

@st.cache_data
def load_data():
    site_info = pd.read_csv(SITE_INFO_URL)
    technician = pd.read_csv(TECHNICIAN_URL)
    follow_up = pd.read_csv(FOLLOW_UP_URL)
    return site_info, technician, follow_up

# --- botão para limpar cache ---
if st.sidebar.button("🔄 Recarregar dados"):
    st.cache_data.clear()
    st.experimental_rerun()  # recarrega a página para refletir alterações

# --- carrega os dados ---
site_info, technician, follow_up = load_data()

# --- interface ---
st.title("📊 Blade Repair Dashboard")

st.subheader("Site Info")
st.dataframe(site_info)

st.subheader("Technician")
st.dataframe(technician)

st.subheader("Follow Up")
st.dataframe(follow_up)
