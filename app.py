
import streamlit as st
import pandas as pd
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb

"""
# El destruye excels para chestnet
"""
@st.cache_data
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'})
    worksheet.set_column('A:A', None, format1)
    writer.save()
    processed_data = output.getvalue()
    return processed_data

uploaded_file = st.file_uploader("Upload your Excel file")

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    columns = [col for col in df.columns]
    options = st.multiselect(
        'Que columnas quieres alv?',
        columns.copy(),
        columns.copy())
    excel = to_excel(df[options])

    st.download_button(label='📥 Download Current Result',
                       data=excel,
                       file_name='chestxcel.xlsx')
