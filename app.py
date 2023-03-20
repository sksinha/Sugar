import streamlit as st
import pandas as pd
from io import StringIO

st.header('Single File Upload')
uploaded_file = st.file_uploader('Upload a file')
df = pd.read_csv(uploaded_file)
st.write(df)
   
