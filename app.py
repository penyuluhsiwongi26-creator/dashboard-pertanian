import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Pertanian", layout="wide")

st.title("🌾 Dashboard Indikator Pertanian")

uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded_file:
    xls = pd.ExcelFile(uploaded_file)
    sheets = xls.sheet_names

    selected_sheet = st.selectbox("Pilih Sheet", sheets)

    df = pd.read_excel(uploaded_file, sheet_name=selected_sheet)

    st.subheader(f"Data: {selected_sheet}")
    st.dataframe(df)

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns

    if len(numeric_cols) > 0:
        col = st.selectbox("Pilih kolom grafik", numeric_cols)
        st.line_chart(df[col])

        st.subheader("Ringkasan")
        st.write("Total:", df[col].sum())
        st.write("Rata-rata:", df[col].mean())
        st.write("Max:", df[col].max())