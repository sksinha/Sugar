import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
st.header('National Cooperative Database :sunglasses:')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
   # st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    #st.write(dataframe)
    st.dataframe(df, use_container_width=True)
   # edited_df = st.experimental_data_editor(df, num_rows="dynamic")
    #AgGrid(df)
    
sel_state = st.selectbox('**Select state**', df.STATE.unique())
fil_df = df[df.STATE == sel_country]  # filter

# Build a new df based from filter.
new_df = pd.melt(fil_df, id_vars=['STATE'], var_name="feature",
                 value_vars=['OWNERSHIP STATUS (COOP / LEASED / PVT.)', 'OPERATIONAL STATUS DURING SY 2021-22'])
title = f'country name: {sel_state}'
fig = px.bar(new_df, x='feature', y='value',
             height=300, log_y=logy, text_auto=textauto,
             title=title)

with st.expander('**State Info**', expanded=True):
    st.plotly_chart(fig, use_container_width=True)
