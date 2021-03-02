import streamlit as st
from io import StringIO
import pandas as pd

st.write('Hello World.')

uploaded_file = st.file_uploader("Choose a file", type=['csv','txr'])
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True, type=['csv','txt'])
if uploaded_file is not None:
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

