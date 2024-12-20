import streamlit as st

st.title("halaman menabung")

# formulir input
with st.form("menabung"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0)
    tanggal = st.date_input("Tanggal")
    waktu = st.time_input("Waktu")
    submit_button = st.form_submit_button(label="Menabung")

    if submit_button and jumlah >= 50000:
        st.session_state["total_semua"].append({
            "Tipe" : "Menabung",
            "jumlah" : jumlah
        })
        st.success("menabung berhasil")
    else:
        st.error("menabung gagal")
