import streamlit as st
import pandas as pd
import numpy as np

## Header
st.header("Load Dataset")

## Dataframe
df = pd.read_csv('https://gist.githubusercontent.com/hbuddana/4f32e8e8b1bcfa39c146ae8dde81b9a0/raw/f9f94e3818d37b3286e744b961432b6a4cf64fbe/Salesdata.csv')
st.dataframe(df)
# st.write(df, width=100, height=500, unsafe_allow_html=True)
# st.code(df,language='Python')
# st.write(df, width=4000, height=500)