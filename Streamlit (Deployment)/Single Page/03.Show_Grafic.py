## Line Chart
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv('https://gist.githubusercontent.com/hbuddana/4f32e8e8b1bcfa39c146ae8dde81b9a0/raw/f9f94e3818d37b3286e744b961432b6a4cf64fbe/Salesdata.csv')

# Judul aplikasi
st.title('Line Chart with Streamlit')
# ----------------------------------------------------------

# Tampilkan dataframe (opsional)
st.dataframe(df)
# ----------------------------------------------------------


# Membuat line chart dengan Plotly Express
st.text(" ")
st.text("Example Line Chart")
st.line_chart(df, x='Region', y='Units')

## Area Chart
st.text(" ")
st.text("Example Area Chart")
st.area_chart(df, x='Region', y='Units')

## Bar Chart
st.text(" ")
st.text("Example Bar Chart")
st.bar_chart(df, x="Region", y="Units")

## Pyplot
st.text(" ")
st.text("Example Pyplot")
x = df['Region']
y = df['Units']
plt.plot(x, y)
plt.xlabel('Region')
plt.ylabel('Units')
plt.title('Example Pyplot')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)