import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
   
dataframe = pd.read_csv(uploaded_file)
st.write(dataframe)
   
