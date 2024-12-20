import streamlit as st

st.title("halaman dashboard")
st.image("unduhan.jpg", caption="gambar rumah")

# fungsi menghitung dan menyimpan total
def total():
    total_nabung = sum(i["jumlah"]
                        for i in st.session_state ["total_semua"]
                        if i ["Tipe"] == "Menabung")
    
    return total_nabung

total_semua = st.session_state["total_semua"]
total_nabung = total()

st.metric("Total_Menabung", f"Rp {total_nabung}")


    