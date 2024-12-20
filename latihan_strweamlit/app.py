import streamlit as st

Dashboard = st.Page("./fitur/dashboard.py", title="dashboard")
Nabung = st.Page("./fitur/nabung.py", title="menabung")

pg = st.navigation(
    {
     "menu utama": [Dashboard],
     "transaksi": [Nabung],

    }
)

if "total_semua" not in st.session_state:
    st.session_state[ "total_semua" ] = []

pg.run()