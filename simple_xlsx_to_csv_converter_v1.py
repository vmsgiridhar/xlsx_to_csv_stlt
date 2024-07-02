# import statements

import streamlit as st
import pandas as pd
import pdb

# content of the app
st.title(body=':blue[XLSX to CSV converter]', help='Giri\'s pet project')
uploaded_files = st.file_uploader("Choose a XLSX file", type=['xlsx','xls'],accept_multiple_files=True,help='File size restricted to 200 MB')
for uploaded_file in uploaded_files:
    if not uploaded_file.name.startswith("~") and uploaded_file.name.endswith(".xlsx"):
        name_of_file = uploaded_file.name.split('.')[0]
        file_extension = uploaded_file.name.split('.')[1]
        if file_extension == 'xlsx':
            df = pd.read_excel(uploaded_file.name, engine='openpyxl')
        elif file_extension == 'xls':
            df = pd.read_excel(uploaded_file.name)
    st.write(f'Converting {uploaded_file.name} to {name_of_file}.csv')
    try:
        df.to_csv(name_of_file + '_converted.csv',index=False)
        st.write(f':green[Completed!]')
    except Exception as e:
        st.write(f':red[Exception is: {e}]')