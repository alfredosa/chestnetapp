import pandas as pd
import streamlit as st

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')
"""
# El destruye excels para chestnet
"""
df = ""
with st.form("Excel mamaleen"):
    user = st.text_input("username", "chestnet")
    password = st.text_input("password", type="password")
    uploaded_file = st.file_uploader("Upload your Excel file")
    submitted = st.form_submit_button("Submit")
    if submitted and password == "MeLaPelas123":
        if uploaded_file is not None:
            df = pd.read_excel(uploaded_file)
        columns = [col for col in df.columns]
    else:
        st.write("La clave no sirve")

if df and columns:
    with st.form("Excel mamaleen"):
        options = st.multiselect(
            'Que columnas quieres alv?',
            columns,
            columns)
        submitted = st.form_submit_button("Submit")
        if submitted:
            csv = convert_df(df)

            st.download_button(
                "Press to Download",
                csv,
                "file.csv",
                "text/csv",
                key='download-csv'
        )
