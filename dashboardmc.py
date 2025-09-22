import streamlit as st
import pandas as pd

# ---------- Links CSV do Google Sheets ----------
SITE_INFO_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQzXWytMh8Iaftl22CHZ201Z32-Exn4sXEZeYSbhYd14xJNjQRriAbU7iIEy97cMe4RdbOzgGtMVgqy/pub?gid=0&single=true&output=csv"
TECHNICIAN_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQzXWytMh8Iaftl22CHZ201Z32-Exn4sXEZeYSbhYd14xJNjQRriAbU7iIEy97cMe4RdbOzgGtMVgqy/pub?gid=47045310&single=true&output=csv"
FOLLOW_UP_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQzXWytMh8Iaftl22CHZ201Z32-Exn4sXEZeYSbhYd14xJNjQRriAbU7iIEy97cMe4RdbOzgGtMVgqy/pub?gid=591517216&single=true&output=csv"

# ---------- Função para carregar dados ----------
@st.cache_data
def load_data():
    site_info = pd.read_csv(SITE_INFO_URL)
    technician = pd.read_csv(TECHNICIAN_URL)
    follow_up = pd.read_csv(FOLLOW_UP_URL)
    return site_info, technician, follow_up

# ---------- Sidebar: botão recarregar ----------
if st.sidebar.button("🔄 Recarregar dados"):
    st.cache_data.clear()
    st.experimental_rerun()

# ---------- Carregar dados ----------
site_info, technician, follow_up = load_data()

# ---------- Interface ----------
st.title("📊 Blade Repair Dashboard")

tabs = st.tabs(["Site Info", "Technician", "Follow Up"])

with tabs[0]:
    st.subheader("Site Info")
    filter_site = st.text_input("Filtrar Site Name (contém)")
    df_filtered = site_info[site_info['Site Name'].str.contains(filter_site, case=False, na=False)]
    st.dataframe(df_filtered)

with tabs[1]:
    st.subheader("Technician")
    filter_name = st.text_input("Filtrar Name (contém)")
    df_filtered = technician[technician['Name'].str.contains(filter_name, case=False, na=False)]
    st.dataframe(df_filtered)

with tabs[2]:
    st.subheader("Follow Up")
    filter_wo = st.text_input("Filtrar WO (contém)")
    df_filtered = follow_up[follow_up['WO'].astype(str).str.contains(filter_wo, case=False, na=False)]
    st.dataframe(df_filtered)
